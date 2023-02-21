
function func1(){
  const  lotno = [1002,4454,1234,5567,6743]

  const x = lotno[Math.floor(Math.random() * lotno.length)]
  
  // id (ranum)
  document.getElementById('ranum').innerHTML = x

  // console.log
  console.log(x)
  
  // id (ran)
  document.getElementById('ran').innerHTML = x

}