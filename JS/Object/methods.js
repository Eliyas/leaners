
const employee = {
    name: "eliyas",
    empId: 104,
    fullAddress: "no: 12, 2nd street mazjith colony, TN, CH-73",
    addressDetail: {
        doorNo: 12,
        street: "2nd street",
        area: "mazjith colony, sembakkam",
        city: "chennai",
        state: "TN",
        postalCode: 73,
        location: ["123322.2323", "435342.5353"] 
    },
    skills: ["JS", "Java", "HTML"]
}

console.log("Values 1 :", Object.values(employee))
console.log("Keys 1 :", Object.keys(employee))


// function declaration
function myValues(employeeObj) {
    const values = [];
    for(let key in employeeObj) {
        const value = employeeObj[key];
        values.push(value);
    }
    return values;
}

function myKeys(employeeObj) {
    const keys = [];
    for(let key in employeeObj) {
        keys.push(key);
    }
    return keys;
}


let result1 = myKeys(employee);
console.log("Values 2 :", myValues(employee));
console.log("Keys 2 :", result1);
