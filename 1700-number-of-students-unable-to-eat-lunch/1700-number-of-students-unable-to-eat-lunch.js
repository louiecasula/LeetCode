/**
 * @param {number[]} students
 * @param {number[]} sandwiches
 * @return {number}
 */
var countStudents = function(students, sandwiches) {
    let counter = 0;
    // Keep iterating while the counter < size of students OR zero
    while (counter < students.length && students.length > 0) {
        // If the first student === first sandwich, shift student and sandwich, set counter to zero
        let first = students.shift();
        if (first === sandwiches[0]) {
            sandwiches.shift();
            counter = 0;
        }
        // Else, shift and push student, increment counter
        else {
            students.push(first);
            counter++;
        }
    }
    // Return size of students
    return students.length;
};