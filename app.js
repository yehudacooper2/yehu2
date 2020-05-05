// console.log('yehuda cooper3');
// var Person = /** @class */ (function () {
//     function Person() {
//         console.log('object created');
//     }
//     return Person;
// }());
// var person1 = new Person();
function findString(str,start,end){
  let string1 = "";
  if(str.includes(start)){
      for(let i = 0;i<=str.length;i++){
          console.log(i);
          if(str[i] == start){
              for(;i<=str.length;i++){
                  if(str[i] == end){
                      break;
                  }
                  string1 += str[i++]
              }
          }
      }
  }
  return string1;
}
console.log(findString("[h]yehudacooper[g]","[h]","[g]"));
console.log("jjj");