// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.8.2 <0.9.0; //Pragma directive to inform that code needs to be run between these solidity versions

contract LotteryContract{

    // initializing state variables
    address public manager;
    address payable[] public candidates;
    address payable public winner;

    constructor(){
        manager = msg.sender; // initialise the owner of this contract into a variable
    }

    receive() external payable{
        require (msg.value == 0.000001 ether); //can only put in 0.000001 ether into this lottery
        candidates.push(payable(msg.sender)); //add this candidate into the candidates array
    }

    function getBalance() public view returns (uint){
        require (msg.sender == manager); //only the manager can use this function
        return address(this).balance; //obtain the balance in this contract
    }

    // pseudorandom function modified from https://medium.com/coinmonks/how-to-generate-random-numbers-in-solidity-16950cb2261d
    // The idea is to generate random number by hashing the blockhash, timestampand transaction origin.
    // other methods either require spending other tokens or require more than 1 transaction
    // downside is that miners can theoretically generate these values before submitting the block i.e. less secure
    function random() internal view returns (uint256) {
    return uint256(keccak256(abi.encodePacked( //abi.encodePacked combines raw representations of parameters into a 52bit array that is sent to keccak256 for hashing
      tx.origin,
      blockhash(block.number - 1), // blockhash 1 block prior
      block.timestamp //timestamp of current block
    )));
  }
    
    //another random function that uses block difficulty, block.timestamp and candidates length
    function getRandom() public view returns (uint){
        return uint(keccak256(abi.encodePacked(
        block.difficulty, 
        block.timestamp, 
        candidates.length)));
    }

    function PickWinner() public {
        require(msg.sender == manager); // ensure only the manager can call this function
        require(candidates.length >= 2); //ensure contract has at least 2 candidates
        uint r = getRandom();
        uint index = r%candidates.length; // obtain winning index
        winner = candidates[index]; // find the winning address

        winner.transfer(getBalance()); //transfer winnings to winner
        candidates = new address payable[](0); //reset candidates array
    }

}