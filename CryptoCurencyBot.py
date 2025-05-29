from colorama import Fore, Style

# Step 1: Define the Cryptocurrency Data
CRYPTO_DATA = {
    "Bitcoin": {
        "price_usd": 68000,
        "price_trend_7d": 5.5,  # Percentage change in the last 7 days
        "energy_efficiency": "C",  # A (Best), B (Good), C (Fair), D (Poor)
        "project_viability": 8,  # Score out of 10 (community, tech, use-case)
        "description": "The pioneering cryptocurrency, known for its decentralized nature and store of value properties. Energy consumption is a concern."
    },
    "Ethereum": {
        "price_usd": 3500,
        "price_trend_7d": 12.1,
        "energy_efficiency": "B",  # Post-Merge (Proof-of-Stake)
        "project_viability": 9,
        "description": "A leading platform for decentralized applications (dApps) and smart contracts. Significantly improved energy efficiency after 'The Merge'."
    },
    "Cardano": {
        "price_usd": 0.45,
        "price_trend_7d": -2.3,
        "energy_efficiency": "A",
        "project_viability": 7,
        "description": "A proof-of-stake blockchain platform focusing on scalability, sustainability, and interoperability, with a strong academic research foundation."
    },
    "Solana": {
        "price_usd": 170,
        "price_trend_7d": 8.0,
        "energy_efficiency": "B",
        "project_viability": 7, # Has faced some network stability issues but strong ecosystem
        "description": "A high-performance blockchain known for its speed and scalability, supporting dApps and marketplaces. Has had some network outages."
    },
    "EcoCoin": { # Fictional example
        "price_usd": 1.20,
        "price_trend_7d": 15.0,
        "energy_efficiency": "A",
        "project_viability": 9,
        "description": "A fictional eco-friendly cryptocurrency designed for carbon offsetting and sustainable projects."
    },
    "RiskToken": { # Fictional example
        "price_usd": 0.10,
        "price_trend_7d": -15.0,
        "energy_efficiency": "D",
        "project_viability": 3,
        "description": "A fictional high-risk, low-viability token with poor fundamentals."
    },
    "StableGrowthCoin": { # Fictional example
        "price_usd": 50,
        "price_trend_7d": 1.5,
        "energy_efficiency": "A",
        "project_viability": 8,
        "description": "A fictional coin focused on steady growth and strong sustainable practices."
    }
}

# Step 2: Design the Chatbot's Core Logic (Rules)
def get_profitability_score(trend):
    """
    Analyzes price trend to determine profitability score.
    Returns: a score from 1 (low) to 5 (high) and a textual description.
    """
    if trend > 10:
        return 5, "Strongly Positive Trend"
    elif trend > 5:
        return 4, "Positive Trend"
    elif trend >= -2: # Includes stable and slightly positive up to 5%
        return 3, "Stable / Slightly Positive Trend"
    elif trend >= -10:
        return 2, "Slightly Negative Trend"
    else:
        return 1, "Strongly Negative Trend"

def get_sustainability_score(energy, viability):
    """
    Analyzes energy efficiency and project viability for sustainability score.
    Returns: a score from 1 (low) to 3 (high) and a textual description.
    """
    # Energy efficiency mapping (higher is better)
    energy_map = {"A": 3, "B": 2, "C": 1, "D": 0}
    energy_val = energy_map.get(energy.upper(), 0)

    # Viability mapping (higher is better)
    if viability >= 8:
        viability_val = 3
    elif viability >= 5:
        viability_val = 2
    else:
        viability_val = 1
    
    total_sustainability_score = energy_val + viability_val # Max 6

    if total_sustainability_score >= 5: # e.g., A energy (3) + high viability (3) = 6
        return 3, "High Sustainability"
    elif total_sustainability_score >= 3: # e.g., B energy (2) + medium viability (2) = 4
        return 2, "Medium Sustainability"
    else:
        return 1, "Low Sustainability"

def generate_advice(crypto_name):
    """
    Generates investment advice for a given cryptocurrency.
    """
    if crypto_name not in CRYPTO_DATA:
        return f"{Fore.RED}Sorry, I don't have data for that cryptocurrency.{Style.RESET_ALL}", None, None, None

    data = CRYPTO_DATA[crypto_name]
    trend = data["price_trend_7d"]
    energy = data["energy_efficiency"]
    viability = data["project_viability"]
    description = data["description"]
    price = data["price_usd"]

    profit_score, profit_desc = get_profitability_score(trend)
    sustain_score, sustain_desc = get_sustainability_score(energy, viability)

    advice = f"\n--- Analysis for {crypto_name} ---\n"
    advice += f"Current Price: ${price:,.2f}\n"
    advice += f"Description: {description}\n"
    advice += f"Profitability Factor: {profit_desc} ({trend}% 7-day change).\n"
    advice += f"Sustainability Factor: {sustain_desc} (Energy: {energy}, Viability: {viability}/10).\n\n"
    advice += "Investment Advice: "

    # Rule-based advice generation
    if profit_score >= 4 and sustain_score == 3: # High Profit, High Sustain
        advice += "Strong Buy. Looks promising on both profit and sustainability fronts."
    elif profit_score >= 4 and sustain_score == 2: # High Profit, Med Sustain
        advice += "Cautious Buy. Good profit potential, but keep an eye on sustainability aspects."
    elif profit_score >= 4 and sustain_score == 1: # High Profit, Low Sustain
        advice += "Risky Buy / Speculative. Potential for short-term gains, but long-term sustainability is a concern. High risk."
    elif profit_score == 3 and sustain_score == 3: # Stable/Slight Profit, High Sustain
        advice += "Consider for Long-Term Hold. Good sustainability, price is relatively stable or slightly positive."
    elif profit_score == 3 and sustain_score == 2: # Stable/Slight Profit, Med Sustain
        advice += "Neutral / Hold. No strong buy or sell signals currently. Monitor for changes."
    elif profit_score <= 2 and sustain_score == 3: # Low/Neg Profit, High Sustain
        advice += "Potential Undervalued / Monitor. Sustainability is strong, but current price trend is not favorable. Could be a long-term opportunity if fundamentals remain solid."
    elif profit_score == 3 and sustain_score == 1: # Stable/Slight Profit, Low Sustain
        advice += "Consider Reducing Exposure. Sustainability is a concern, even if the price is currently stable."
    elif profit_score <= 2 and sustain_score == 2: # Low/Neg Profit, Med Sustain
        advice += "Caution / Monitor Closely. Both profitability and sustainability are not ideal. Re-evaluate your position."
    elif profit_score <= 2 and sustain_score == 1: # Low/Neg Profit, Low Sustain
        advice += "Strong Sell / Avoid. Significant concerns on both profitability and sustainability fronts."
    else: # Catch-all for any unhandled combinations, though the above should cover most.
        advice += "Difficult to assess with current rules. Further research recommended."
        
    advice += "\n\nNote: This advice is based on a simplified model and should not replace thorough research and professional financial advice."
        
    return advice, profit_desc, sustain_desc, description

# Step 3: Implement the Chatbot Conversation Flow
def get_user_input():
    """
    Gets user input and normalizes it to match dictionary keys.
    """
    user_input = input("\nWhich cryptocurrency are you interested in? ").strip().lower()
    if user_input == 'exit':
        return user_input
    
    # Normalize input to match dictionary keys
    for crypto in CRYPTO_DATA.keys():
        if crypto.lower() == user_input:
            return crypto
    return None

def chatbot():
    """
    Main function to run the chatbot conversation.
    """
    print("Welcome to the Crypto Investment Advisor Chatbot!")
    print("I can provide basic investment advice based on profitability and sustainability factors.")
    print("Disclaimer: This is not financial advice. Always do your own research (DYOR).\n")

    while True:
        print("\nAvailable cryptocurrencies:")
        for crypto in CRYPTO_DATA.keys():
            print(f"- {crypto}")
        print("- Type 'exit' to quit.")

        crypto_name = get_user_input()
        if crypto_name == 'exit':
            print("Thank you for using the Crypto Advisor. Goodbye!")
            break
        elif crypto_name is None:
            print(Fore.RED + "SORRY, I DON'T HAVE DATA FOR THAT CRYPTOCURRENCY" + Style.RESET_ALL)
            continue

        advice, _, _, _ = generate_advice(crypto_name)
        print(advice)

if __name__ == "__main__":
    chatbot()