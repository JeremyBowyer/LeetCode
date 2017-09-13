// https://leetcode.com/problems/keyboard-row/description/

/**
 * @param {string[]} words
 * @return {string[]}
 */
var findWords = function(words) {
    
    kbMap = {
        a: "row2",
        b: "row3",
        c: "row3",
        d: "row2",
        e: "row1",
        f: "row2",
        g: "row2",
        h: "row2",
        i: "row1",
        j: "row2",
        k: "row2",
        l: "row2",
        m: "row3",
        n: "row3",
        o: "row1",
        p: "row1",
        q: "row1",
        r: "row1",
        s: "row2",
        t: "row1",
        u: "row1",
        v: "row3",
        w: "row1",
        x: "row3",
        y: "row1",
        z: "row3"
    };
    
    let set = new Set();
    keepers = [];
    
    for (var i = 0; i < words.length; i++) {
        
	    word = words[i];
        set.clear();
        
        for (var c = 0; c < word.length; c++) {
            char = word[c].toLowerCase();
            set.add(kbMap[char]);
        }
        
        if (set.size == 1) {
            keepers.push(word);
        }
    }
    
    return keepers
};