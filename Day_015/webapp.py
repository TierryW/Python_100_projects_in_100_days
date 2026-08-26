import streamlit as st

st.set_page_config(page_title="Coffee Machine", page_icon="☕")

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

if "resources" not in st.session_state:
    st.session_state.resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }

if "profit" not in st.session_state:
    st.session_state.profit = 0.0

if "message" not in st.session_state:
    st.session_state.message = ""

resources = st.session_state.resources

def is_resource_sufficient(order_ingresients):
    for item in order_ingresients:
        if order_ingresients[item] > resources[item]:
            return False, item

    return True, None

def calculate_payment(quarters, dimes, nickles, pennies):
    total = 0
    total += quarters * 0.25
    total += dimes * 0.10
    total += nickles * 0.05
    total += pennies * 0.01

    return round(total, 2)

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    st.session_state.message = (f"☕ Here is your {drink_name}!")

def process_order(drink_name, quarters, dimes, nickles, pennies):
    drink = MENU[drink_name]

    sufficient, missing_resource = is_resource_sufficient(drink["ingredients"])

    if not sufficient:
        st.session_state.message = (f"❌ Sorry, there is not enough {missing_resource}.")
        return

    payment = calculate_payment(quarters, dimes, nickles, pennies)

    if payment < drink["cost"]:
        st.session_state.message = (f"❌ Sorry, that's not enough money. "
            f"${payment:.2f} refunded.")
        return

    change = round(payment - drink["cost"], 2)
    st.session_state.profit += drink["cost"]

    make_coffee(drink_name, drink["ingredients"])
    st.session_state.message = (f"☕ Here is your {drink_name}! "
        f"Change: ${change:.2f}")

st.title("☕ Coffee Machine")
st.write("Welcome! Choose your favorite coffee and insert your coins.")

with st.sidebar:
    st.header("📊 Machine Report")
    st.metric("Water", f"{resources['water']} ml")
    st.metric("Milk", f"{resources['milk']} ml")
    st.metric("Coffee", f"{resources['coffee']} g")
    st.metric("Profit", f"${st.session_state.profit:.2f}")
    st.divider()

    if st.button("🔄 Reset Machine", use_container_width=True):
        st.session_state.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        st.session_state.profit = 0.0
        st.session_state.message = ""

        st.rerun()

st.subheader("Choose your drink")
choice = st.selectbox(
    "What would you like?",
    options=[
        "espresso",
        "latte",
        "cappuccino"
    ]
)

drink = MENU[choice]

st.info(f"💰 Price: ${drink['cost']:.2f}")

st.subheader("Ingredients")

for ingredient, amount in drink["ingredients"].items():
    if ingredient == "water":
        st.write(f"Water: {amount} ml")
    elif ingredient == "milk":
        st.write(f"Milk: {amount} ml")
    elif ingredient == "coffee":
        st.write(f"Coffee: {amount} g")

st.divider()

st.subheader("💰 Insert coins")

col1, col2 = st.columns(2)
with col1:
    quarters = st.number_input(
        "Quarters ($0.25)",
        min_value=0,
        step=1
    )
    dimes = st.number_input(
            "Dimes ($0.10)",
            min_value=0,
            step=1
    )

with col2:
    nickles = st.number_input(
        "Nickles ($0.05)",
        min_value=0,
        step=1
    )
    pennies = st.number_input(
            "Pennies ($0.01)",
            min_value=0,
            step=1
    )

payment = calculate_payment(quarters, dimes, nickles, pennies)
st.write(f"**Total inserted: ${payment:.2f}**")

if st.button(
    "☕ Make Coffee",
    type="primary",
    use_container_width=True
):
    process_order(choice, quarters, dimes, nickles, pennies)
    st.rerun()

if st.session_state.message:
    message = st.session_state.message
    if message.startswith("☕"):
        st.success(message)
    else:
        st.error(message)
