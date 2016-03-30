print pascal(int(input("enter number"))
def pascal(depth) {
  var count = 1;
  var mult = []
  while(count <= depth) {
    if(count == 1) {
      mult.push([1]); 
      count++;
    }
    else if(count == 2) {
      mult.push([1,1])
      count++;
    }
    else {
      var x = [];
      var y = 0;
      while(y < count) {
        if(y == 0 || y == count - 1) { 
          x.push(1);
          y++;
        }
        else {
          x.push((mult[count - 2][y - 1] + mult[count - 2][y]));
          y++;
        }
     }
     mult.push(x);
     count++;
     }
  }     
  return mult
}