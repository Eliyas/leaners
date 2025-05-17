// object declaration and initialization
const myObj = {};

//or
const eliyas = new Object();

// assign values 1st way
eliyas.name = "Eliyas";
eliyas.age = 18;

// assign values 2nd way
eliyas["email"] = "saif@gmail.com";

// accessing properties values
console.log("Eliyas Name is :" + eliyas.name);
console.log("Eliyas Name is :" + eliyas["email"]);

// object with properties
// key:  value = property
// name: "Crow",
const bird = {
    // properties
    name: "Crow",
    color: "Black",
    weightInGrams: 100,
    gender: "boy",
    favoriteFoods: ["rice", "meat", "rate"],

    // methods
    fly: () => {},
    sound: () => {},
    eat: () => {},
    bath: () => {}
}


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

employee.addressDetail.state = "Tamil Naadu";
employee["addressDetail"]["state"] = "Kerala";

const addressKey = "addressDetail";
const stateKey = "state";
console.log("Employee State 1: "+ employee["addressDetail"]["state"]);
console.log("Employee State 2: "+ employee[addressKey][stateKey]);

const myKeyObj = {
    empIdKey: "empId"
}

// 1 step by step execution
// step 1 => employee[myKeyObj.empIdKey]
// step 2 => employee["empId"]
// step 3 => 104

// 2 step by step execution
// step 1 => employee.name
// step 2 => "eliyas"

// 3 step by step execution
// step 1 => employee["name"]
// step 2 => "eliyas"

console.log("Employee Id: "+ employee[myKeyObj.empIdKey]);

let otherKeyObj = "name";

console.log("Employee Id: "+ employee[otherKeyObj]);

console.log("Employee Name :" + employee.name);
console.log("Employee Name :" + employee["name"]);

console.log("Employee City :" + employee.addressDetail.city);
console.log("Employee City :" + employee.addressDetail["city"]);
console.log("Employee City :" + employee["addressDetail"]["city"]);