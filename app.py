import streamlit as st
import pandas as pd

# Load rules
rules_sorted = pd.read_csv("association_rules.csv")  # or use your DataFrame if already in memory

# Convert antecedents/consequents to frozensets if they are strings in CSV
def str_to_set(x):
    # Check if x is already a frozenset
    if isinstance(x, str):
        x = x.strip("frozenset({})")
        items = [i.strip().strip("'") for i in x.split(",") if i]
        return set(items)
    else:
        return x

rules_sorted['antecedents'] = rules_sorted['antecedents'].apply(str_to_set)
rules_sorted['consequents'] = rules_sorted['consequents'].apply(str_to_set)

# --- THIS MUST COME BEFORE MULTISELECT ---
all_items = sorted(list(set([i for s in rules_sorted['antecedents'] for i in s] +
                            [i for s in rules_sorted['consequents'] for i in s])))

# Multi-select box
selected_items = st.multiselect("Select items you want to buy:", all_items)

# Recommendation function
def recommend_items(selected_items, rules=rules_sorted, top_n=5):
    recommendations = {}
    for _, row in rules.iterrows():
        if row['antecedents'].issubset(set(selected_items)):
            for item in row['consequents']:
                if item not in selected_items:
                    recommendations[item] = max(recommendations.get(item, 0), row.get('lift', 0))
    recommended_sorted = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    return [item for item, _ in recommended_sorted[:top_n]]

# Button to show recommendations
if st.button("Get Recommendations"):
    if selected_items:
        recommendations = recommend_items(selected_items)
        if recommendations:
            st.success("You may also consider buying:")
            for item in recommendations:
                st.write(f"- {item}")
        else:
            st.info("No strong recommendations found for the selected items.")
    else:
        st.warning("Please select at least one item.")
