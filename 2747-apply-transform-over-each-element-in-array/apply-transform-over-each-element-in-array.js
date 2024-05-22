/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const res = [] 
    arr.forEach((key, value) => {
        res.push(fn(key, value))
    })
    return res
    
};