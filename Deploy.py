import web3
from web3 import Web3
from solcx import compile_source

# Solidity source code
with open("student_management.sol", "r") as f:
    contract_source_code = f.read()

# Compile the contract
compiled_sol = compile_source(contract_source_code, output_values=["abi", "bin"])

# Retrieve the contract interface
contract_id, contract_interface = compiled_sol.popitem()

# Get bytecode / bin
bytecode = contract_interface["bin"]

# Get ABI
abi = contract_interface["abi"]

# Web3.py instance
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

# Set pre-funded account as sender
w3.eth.default_account = w3.eth.accounts[0]

# Deploy the contract with constructor arguments
student_management = w3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = student_management.constructor("Mainuzzaman", 27, "enrolled", [90, 85, 95]).transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

# Instantiate the contract at the deployed address
student_management = w3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=abi
)

# Interact with the contract using its functions
def add_student (name, age, enrollStatus, grades):
    student_management.functions.addStudent(name, age, enrollStatus, grades).transact()

add_student("Sajid", 26, "enrolled", [80, 85, 90])

def view_function(studentID):
    student = student_management.functions.getStudents(studentID).call()
    return student

print(view_function(2))

def updateStudentInfo(id, enrolledStatus):
    student_management.functions.updateStudentInfo(id, enrolledStatus).transact()
    return view_function(id)

updateStudentInfo(2, 'not enrolled')

def updateStudentAge(id, age):
    student_management.functions.updateStudentAge(id, age).transact()
    return view_function(id)

print(updateStudentAge(2, 25))

