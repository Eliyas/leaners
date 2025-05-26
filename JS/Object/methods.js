
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

// console.log("Values 1 :", Object.values(employee))
// console.log("Keys 1 :", Object.keys(employee))


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
// console.log("Values 2 :", myValues(employee));
// console.log("Keys 2 :", result1);


// 1. Object reference

// let name1 = "burhan";
// let name2 = name1;
// name2 = "basith";

// console.log("name1 : ", name1);
// console.log("name2 : ", name2);

let employee1 = {
    name: "burhan",
    companyName: "Google",
    companyPlace: "Chennai"
}

let employee2 = employee1;

employee2.name = "basith";

employee1.companyName = "TVS";

console.log("employee1 : ", employee1.name);
console.log("employee1 company : ", employee1.companyName);
console.log("employee2 : ", employee2.name);
console.log("employee2 company : ", employee2.companyName);


// to cut the reference
let employee3 = {
    name: "burhan",
    companyName: "Google",
    companyPlace: "Chennai"
}

let employee4 = { ...employee3 };
let employee5 = Object.create(employee3);

employee4.name = "basith";

employee3.companyName = "TVS";

console.log("employee3 : ", employee3.name);
console.log("employee3 company : ", employee3.companyName);
console.log("employee4 : ", employee4.name);
console.log("employee4 company : ", employee4.companyName);



function myCreate1(object) {
    let newObject = {};

    // copy the properties from object to newObject
    newObject = {...object};

    return newObject;
}


function myCreate2(object) {
    let newObject = {};

    for(let key in object) {
        console.log("Key : ", key);
        console.log("value : ", object[key]);
        newObject[key] = object[key];
    }

    return newObject;
}

console.log("copied Object : ", myCreate1(employee3));
console.log("copied Object : ", myCreate2(employee3));