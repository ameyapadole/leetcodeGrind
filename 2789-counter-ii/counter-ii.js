/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let currentCount = init
    return {
       increment : () => {
        return currentCount += 1
       },

        decrement: function(){
            return currentCount -= 1
        },

        reset: function() {
            return (currentCount = init)
        }
    }
    
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */