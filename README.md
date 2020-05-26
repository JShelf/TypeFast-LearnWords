# Learn to type and learn some words at the same time.

## Steps
### Word Learning
* Dictionary from this [github page](https://raw.githubusercontent.com/matthewreagan/WebstersEnglishDictionary/master/dictionary_compact.json) (really high availability <3mb) it's got some abbreviations so those might need to be filtered
* Grabs uncommon/interesting words
  * ~~How do I determine they are uncommon or interesting?~~
    * Take the most common [10000 words](https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english.txt) 
      * XOR with the original dictionary
      * Top 10000 words accounts for 97.3% of words used 
  * Filter out all articles/abbreviations/pluralization
* Just store it in local after this for quick access as local file.

### Typing
* Experience really similar to keybr.com
* Grabs a bunch of the words approximately 50 letter strings
* Separates them by space
* Track data
* Settings just like BR
  * Prompt Length
  * Capitals
  * Punctuation



### MVP
* launchable client 
* prompts user with sentence with atleast one interesting word
* dictionary link to that word or a way to hover it and see what the word means


### Architecture
* Backend on Node.js
  * Main page(Typing Game/Dictionary) will be on a scalable node
  * Everything else: login, stats, options will be together and non-scalable
* Docker for quick deployment
* CI/CD
  * ???
* AWS EC2 behind cloudflare
* Eventually Kubernetes???