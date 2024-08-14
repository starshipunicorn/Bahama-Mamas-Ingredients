import streamlit as st

# CSS for blue/pink theme and improved styling
st.markdown(
    """
    <style>
    body {
        background-color: #f0f0f5;
        font-family: 'Arial', sans-serif;
    }
    .stSelectbox label {
        font-size: 18px;
        color: #3333cc;
    }
    .stSelectbox div {
        color: #ff3399;
    }
    .stMarkdown {
        background-color: #ffffff;
        padding: 10px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
    }
    ul {
        color: #3333cc;
        font-size: 16px;
    }
    li {
        margin-bottom: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the app
st.title("🍸 Drink Ingredients Finder")

# Dictionary containing your drinks and ingredients
drinks = {
    "Orange Cosmo": ["Bahama Vodka", "Orange Juice", "Triple Sec", "Cranberry Juice"],
    "Blue Lagoon": ["Curacao", "Pineapple Juice", "Lemonade", "Bahama Vodka", "Special Ing"],
    "Purple Rain": ["Curacao", "Sweet & Sour Mix", "Bahama Vodka", "Cranberry Juice"],
    "Pink Apple Martini": ["Sour Apple Liqueur", "Simple Syrup", "Bahama Vodka", "Lemon Juice"],
    "Old Lady": ["Apple Brandy", "Grenadine", "Lemon Juice", "Bahama Gin"]
}

# Dropdown menu for selecting a drink
selected_drink = st.selectbox("Select a drink:", ["Choose..."] + list(drinks.keys()))

# Display ingredients in a list format if a drink is selected
if selected_drink and selected_drink != "Choose...":
    st.markdown("<ul>" + "".join([f"<li>{ingredient}</li>" for ingredient in drinks[selected_drink]]) + "</ul>", unsafe_allow_html=True)

