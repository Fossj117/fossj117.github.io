---
layout: post
title: "A Bluffing Game of Chicken on Ethereum"
date: 2024-01-21
latex: true
mathjax: true
comments: true
tag: ["web3", "art"]
---

I was trying to think of weird simple things that I could try to [implement in Solidity](https://jeffreyfossett.com/2024/01/16/implementing-something-simple-in-solidity.html). Here is an idea for a game I came up with. It's inspired by the [game of chicken](https://en.wikipedia.org/wiki/Chicken_(game)), and also the board game [Coup](https://boardgamegeek.com/boardgame/131357/coup) I was playing recently. I am not 100% sure whether it is possible, but I think it might be? If you know more about Solidity / Ethereum than I do, please let me know. Anyway, here is the game. 

Let $X$ be the "stakes" of the game. 

I start the game by deploying a version of the game's smart contract and putting in $X$ ETH and revealing the first $K$ bits of my (256-bit) private key. 

You can challenge me by also putting up $X$ ETH, and revealing the first $K' > K$ bits of your private key. 

Then, it is my turn again. I have three options. I can: 

1. **Raise**: deposit another $X$ ETH and reveal $K'' > K'$ bits. 
2. **Fold**: give up and concede all the ETH in the contract to you. 
3. **Call your bluff**: if I do this, I post an additional $X$ ETH and you have to post the rest of your private key (starting with the $K'$ bits currently posted) and a new wallet address. 
    * If you were bluffing, I get all the ETH in the contract. 
    * If you were telling the truth, you get all the ETH in the contract (sent to the new wallet you posted). 

If I choose to "raise", the game goes back to you and you have the same choices. The game continues until someone folds or calls a bluff. If someone fails to respond within some amount of time, they automatically concede the game. 

Some possible variants: 
* Maybe you can only if you have at least $10X$ ETH in your wallet (to make sure there are "stakes" to revealing your key). This would definitely influence the game payoffs / desirability of bluffing. 
* I'm not sure if you should be able to post a whole new set of bits each round, or just a marginal bit. I think probably the former is more fun to allow for gamesmanship -- e.g. if I posted a set of $K$ bits last turn and now I post a new longer set of bits that are not compatible with the set I already posted, you know I must have been lying (or I am lying now!). 
* Maybe the "stakes" to continue should escalate each turn (e.g. on the first round you have to post $X$ ETH, on the second you have to post $2X$ and so on). 

I'm not 100% sure about implementing this game on Ethereum, but I think it might be possible. Per some discussion about a similar idea with [Kassandra](https://github.com/kassandraoftroy) a while back, I think there is also a potential issue with front-running transactions in the mempool in the bluff call situation. For example, if I have to post my full private key to prove that I was not bluffing, then someone else could see that transaction come into the mempool, and then front-run my transaction pretending to be me and claim the ETH in the contract to a new wallet address of their choosing. I am not sure if there might be a fancy [zero-knowledge](https://en.wikipedia.org/wiki/Zero-knowledge_proof) type workaround for this issue. I.e. if you call my bluff, is there a way for me to prove that I am not lying about the bits I have posted so far without having to reveal my whole key for verification? 

If you have ideas about this, email me at `fossj117 AT gmail DOT com`. I haven't thought about this game too hard (it's just for fun anyways), so maybe there's some obvious room for improvement. Let me know!