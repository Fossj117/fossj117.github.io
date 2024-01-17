---
layout: post
title: "Implementing Something Simple in Solidity"
date: 2024-01-16
latex: true
mathjax: true
comments: true
tag: ["web3"]
---

## Setup

I have never attempted to write any Solidity code, so today I am going set myself the challenge of implementing (and maybe deploying) something simple, so that I can better understand how smart contracts and the whole Ethereum world works.

What I have chosen to implement is an NFT collection of four assets which will represent the ownership of different quadrants (top left, top right, bottom left, bottom right) of an image that I will display below on this page. The owner of a given asset will be able send a message to the contract to update the color of their quadrant (by sending a hex code). The image on this page will read the current colors stored in the contract on page load and render them.

## Implementation 

I am starting by setting up my development environment according to instructions from ChatGPT. I'll be using [`truffle`](https://trufflesuite.com/) per GPT's recommendation. Since my concept is a variant of an NFT collection, I think an easy approach is to build on an existing openzeppelin implementation. [Here are docs on the basic ERC721 impelementation](https://docs.openzeppelin.com/contracts/5.x/api/token/erc721#ERC721). From my understanding, I think I only need to add two bits of logic to the base implementation: 

1. A cap on the number of assets that can be minted (I only want there to be four).
2. Color update logic, which includes: 
    * Storing the current colors as public state in some form.
    * Allowing the owner of an NFT to update its color by calling a method on the contract (and passing a new color string). 

Something that is a bit confusing to me about working with OpenZeppelin at the outset is that I don't understand exactly what is in the base implementations that I am inheriting from. Looking at the code [here](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC721/ERC721.sol) is clarifying. With some fiddling and ChatGPT help, here is the contract code that I come up with: 

{% highlight solidity %}
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ColorQuadrantNFT is Ownable, ERC721 {
    // Create a counter that keeps track of the number of NFTs minted
    uint256 private _totalMinted;

    // Map from the token id to the color as a string
    mapping(uint256 => string) private _tokenColors;

    constructor(
        string memory name,
        string memory symbol, 
        address owner
    ) ERC721(name, symbol) Ownable(owner){
        _totalMinted = 0;
    }

    // Simple minting function
    function mintNext(address recipient) public onlyOwner {
        require(_totalMinted < 4, "No more assets can be minted");
        _safeMint(recipient, _totalMinted); //token id is the same as the _totalMinted
        _totalMinted++;
    }

    // function that returns the total number of NFTs minted
    function getTotalMinted() public view returns (uint256) {
        return _totalMinted;
    }

    // function that allows owner of a given NFT to change its color
    function setColor(uint256 tokenId, string memory _color) public {
        require(msg.sender == ownerOf(tokenId), "Only the owner can change the color");
        _tokenColors[tokenId] = _color;
    }

    // function that returns the color of a given NFT
    function getColor(uint256 tokenId)
        public
        view
        returns (string memory)
    {
        return _tokenColors[tokenId];
    }
}
{% endhighlight %}

This is a super basic implementation that doesn't bother to handle any edge cases (I am just doing this for learning purposes). A few notes: 

* Only the owner of the contract is allowed to mint new tokens. 
* Tokens have a `tokenID` from 0 to 3, sequentially.
* Colors are stored on chain as a mapping from `tokenID` to a `string`. 
    * I don't do any checking to confirm that a valid hex color is passed for now.
* Current color of a given token can be accessed via the public `getColor` function. 
    * I don't check if a color has been set already in the mapping. My understanding of solidity is that if a key is not defined in a mapping, it returns the default value for the value type which is an empty string ("") in this case, which is fine. 
* I will handle the color processing logic on the `javscript` frontend. 

My next step is to test this code. I download `ganache` for local testing, and set up a simple migration script. After some fiddling with `ganache` versions and the code, I am able to compile and deploy my contract successfully, and confirm via local testing with `truffle` that it seems to work as expected: I am able to mint up to four assets and change and retrieve their colors. 

That's all that I have time for on this today. In my next iteration on this project, I will set up the front end piece with `web3.js` and try deploying to a testnet. I think that deploying and interacting with a contract I understand on a testnet will help me better understand web3 data [that I am exploring elsewhere](https://jeffreyfossett.com/2024/01/15/rates-of-NFT-project-creation.html), so I am looking forward to that.  