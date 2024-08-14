import streamlit as st

# Dictionary containing your drinks and ingredients
drinks = {
    "Orange Cosmo": ["1 x Bahama Vodka", "1 x Orange Juice", "1 x Triple Sec", "1 x Cranberry Juice"],
    "Blue Lagoon": ["1 x Curacao", "1 x Pineapple Juice", "1 x Lemonade", "1 x Bahama Vodka", "1 x Special Ing"],
    "Purple Rain": ["1 x Curacao", "1 x Sweet & Sour Mix", "1 x Bahama Vodka", "1 x Cranberry Juice"],
    "Pink Apple Martini": ["1 x Sour Apple Liqueur", "1 x Simple Syrup", "1 x Bahama Vodka", "1 x Lemon Juice"],
    "Old Lady": ["1 x Apple Brandy", "1 x Grenadine", "1 x Lemon Juice", "1 x Bahama Gin"]
}

# Title of the app
st.title("Drink Ingredients Finder")

# Dropdown menu for selecting a drink
selected_drink = st.selectbox("Select a drink:", list(drinks.keys()))

# Display ingredients
if selected_drink:
    st.write(f"**Ingredients for {selected_drink}:**")
    st.write(", ".join(drinks[selected_drink]))
