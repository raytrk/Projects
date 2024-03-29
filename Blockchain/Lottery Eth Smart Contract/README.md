# Lottery Smart Contract

## Description:

#### 📜 Summary:

> This Lottery Contract Smart Contract Project was created while learning to create a simple smart contract on the Ethereum blockchain using the Solidity programming language.
> 
> Smart Contract at this address: https://sepolia.etherscan.io/address/0x3cc4d73bff31257ba61a79cabe9f62210663a3bb
<br>

:bulb: **Overall**

 1. This Smart contract was created using the Remix IDE on the Sepolia testnet
 2. Test SepoliaEth was obtained from sepoliafaucet.com using an Alchemy account for gas fees and the ante for the Lottery Contract
 3. In the Lottery Contract, participants can put up an ante of 0.000001 ETH = 1000 Gwei for the chance to receive the entire pot in the contract
 4. Contract creator will pick a winner once there are at least 2 participants in the contract

<br>

👨‍🎓 **Takeaways**

Remix IDE:

 - Remix IDE is used for writing Solidity smart contracts, though VSCode with a solidity extension can be used as well.

State Variables and Initialization:

 - State Variables are stored within the contract and gas fees are required to access these state variables

 Modifiers: 
 - `Payable` allows addresses to receive Ether transfers

Function Visibility:

 - `public`: Accessible from both inside and outside the contract.
 - `private`: Only accessible within the contract.
 - `internal`: Accessible within the contract and contracts inheriting from it.
 - `view`: Can be called without modifying contract state (doesn't spend gas for writes).

 Randomness: Generating randomness in solidity is difficult. There are tradeoffs between security, availability on different blockchains, cost.

 - `keccak256()` hashing allows for generating pseudo-random numbers
 - `abi.encodePacked()` combines raw representations of the parameters passed into a 52 bit array
<br>

## References

1. Coursera course: https://www.coursera.org/projects/smart-contracts-with-solidity-create-an-ethereum-contract
2. Pseudorandom function: https://medium.com/coinmonks/how-to-generate-random-numbers-in-solidity-16950cb2261d
