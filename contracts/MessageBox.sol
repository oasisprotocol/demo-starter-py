// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MessageBox {
    string private _message;
    address public author;

    function setMessage(string calldata in_message) external {
        _message = in_message;
        author = msg.sender;
    }

    function message() external view returns (string memory, address, address) {
        // TODO: Signed queries not supported yet. https://github.com/oasisprotocol/sapphire-paratime/issues/347
        // if (msg.sender != author) {
        // revert("not allowed");
        // }
      return (_message, author, msg.sender);
    }
}