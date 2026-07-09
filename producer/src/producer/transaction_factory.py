from random import choice, randint, uniform
from producer.models import Transaction
from dataclasses import dataclass
from producer.settings import CUSTOMER_COUNT

@dataclass(frozen=True)
class Merchant:
    id: str
    name: str
    category: str
    min_amount_sgd: float
    max_amount_sgd: float

MERCHANT_CATEGORIES = [
    "Groceries",
    "Electronics",
    "Travel",
    "Dining",
    "Fuel",
    "Healthcare",
    "Entertainment",
    "Luxury",
    "Gaming",    
]

# Static reference data
# ---------------------------------------------------------------------

MERCHANTS = [
    Merchant("MRC00000001", "NTUC FairPrice", "Groceries", 5.00, 250.00),
    Merchant("MRC00000002", "Cold Storage", "Groceries", 10.00, 300.00),
    Merchant("MRC00000003", "Sheng Siong", "Groceries", 5.00, 200.00),

    Merchant("MRC00000004", "Apple Store", "Electronics", 300.00, 3500.00),
    Merchant("MRC00000005", "Challenger", "Electronics", 30.00, 1500.00),
    Merchant("MRC00000006", "Best Denki", "Electronics", 100.00, 3000.00),

    Merchant("MRC00000007", "McDonald's", "Dining", 5.00, 40.00),
    Merchant("MRC00000008", "Hai Di Lao", "Dining", 30.00, 250.00),
    Merchant("MRC00000009", "Starbucks", "Dining", 5.00, 35.00),

    Merchant("MRC00000010", "Shell", "Fuel", 20.00, 200.00),
    Merchant("MRC00000011", "Esso", "Fuel", 20.00, 200.00),
    Merchant("MRC00000012", "Caltex", "Fuel", 20.00, 200.00),

    Merchant("MRC00000013", "Guardian", "Healthcare", 5.00, 150.00),
    Merchant("MRC00000014", "Watsons", "Healthcare", 5.00, 180.00),
    Merchant("MRC00000015", "Unity Pharmacy", "Healthcare", 5.00, 200.00),

    Merchant("MRC00000016", "Golden Village", "Entertainment", 10.00, 80.00),
    Merchant("MRC00000017", "Netflix", "Entertainment", 10.00, 30.00),
    Merchant("MRC00000018", "Disney+", "Entertainment", 10.00, 25.00),

    Merchant("MRC00000019", "Louis Vuitton", "Luxury", 800.00, 8000.00),
    Merchant("MRC00000020", "Gucci", "Luxury", 500.00, 6000.00),
    Merchant("MRC00000021", "Rolex Boutique", "Luxury", 5000.00, 30000.00),

    Merchant("MRC00000022", "Steam", "Gaming", 5.00, 120.00),
    Merchant("MRC00000023", "PlayStation Store", "Gaming", 5.00, 150.00),
    Merchant("MRC00000024", "Riot Games", "Gaming", 5.00, 100.00),

    Merchant("MRC00000025", "Singapore Airlines", "Travel", 300.00, 5000.00),
    Merchant("MRC00000026", "Booking.com", "Travel", 100.00, 3000.00),
    Merchant("MRC00000027", "Agoda", "Travel", 80.00, 2500.00),
]

COUNTRIES = ["SG", "MY", "TH", "ID", "US"]

CURRENCY_INFO = {
    "SG": {
        "currency": "SGD",
        "multiplier": 1.00,
    },
    "MY": {
        "currency": "MYR",
        "multiplier": 3.45,
    },
    "TH": {
        "currency": "THB",
        "multiplier": 25.5,
    },
    "ID": {
        "currency": "IDR",
        "multiplier": 12500,
    },
    "US": {
        "currency": "USD",
        "multiplier": 0.74,
    },
}

CHANNELS = ["Online", "POS", "ATM", "Mobile"]
STATUSES = ["SUCCESS", "FAILED", "PENDING"]

# Helper functions
# ---------------------------------------------------------------------

def generate_transaction_id(sequence_number: int) -> str:
    return f"TX{sequence_number:08d}"

def generate_customer():
    """
    Simulate customers.
    Each customer owns exactly one account for now.
    """

    customer_number = randint(1, CUSTOMER_COUNT)

    return {
        "customer_id": f"CUST{customer_number:08d}",
        "account_id": f"ACC{customer_number:08d}",
    }


def generate_merchant() -> Merchant:
    """Return a random merchant."""
    return choice(MERCHANTS)

# Transaction Factory
# ---------------------------------------------------------------------

def create_transaction(sequence_number: int) -> Transaction:

    customer = generate_customer()
    merchant = generate_merchant()

    country = choice(COUNTRIES)
    currency_info = CURRENCY_INFO[country]

    base_amount = uniform(
        merchant.min_amount_sgd,
        merchant.max_amount_sgd,
    )

    local_amount = round(
        base_amount * currency_info["multiplier"],
        2,
    )

    return Transaction(
        transaction_id=generate_transaction_id(sequence_number),
        customer_id=customer["customer_id"],
        account_id=customer["account_id"],
        merchant_id=merchant.id,
        merchant_category=merchant.category,
        amount=local_amount,
        currency=currency_info["currency"],
        country=country,
        channel=choice(CHANNELS),
        status=choice(STATUSES),
    )