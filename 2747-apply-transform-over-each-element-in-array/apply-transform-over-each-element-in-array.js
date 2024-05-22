/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const res = []
    arr.forEach((key, val) => {

        res.push(fn(key, val))

    })    
    return res
};