console.log('js loaded');
let notify = document.getElementById('calculate');
notify.addEventListener('click',function(){
    let height = document.getElementById('height').value;
    let weight = document.getElementById('weight').value;
    let age = document.getElementById('age').value;
    let gender = document.querySelector('input[name="gender"]:checked').value;
    let cuongdo = document.querySelector('input[name="cuongdo"]:checked').value;
    if(gender == "male")
    {
        bmr = 66 + (13.75 * parseInt(weight)) + (5 * parseInt(height)) - (6.7 * parseInt(age));
    }
    else
    {
        bmr = 655 + (9.6 * parseInt(weight)) + (1.8 * parseInt(height)) -  (4.7 * parseInt(age));
    }
    if(cuongdo == 1.2)
    {
        calo = parseInt(bmr) * 1.2;
        calotang = calo + calo * 0.2;
        calogiam = calo - calo * 0.2;
    }
    else if(cuongdo == 1.375)
    {
        calo = parseInt(bmr) * 1.375;
        calotang = calo + calo * 0.2;
        calogiam = calo - calo * 0.2;
    }
    else if(cuongdo == 1.45)
    {
        calo = parseInt(bmr) * 1.45;
        calotang = calo + calo * 0.2;
        calogiam = calo - calo * 0.2;
    }
    else if(cuongdo == 1.75)
    {
        calo = parseInt(bmr) * 1.75;
        calotang = calo + calo * 0.2;
        calogiam = calo - calo * 0.2;
    }
    else if(cuongdo == 1.95)
    {
        calo = parseInt(bmr) * 1.95;
        calotang = calo + calo * 0.2;
        calogiam = calo - calo * 0.2;
    }
    
    console.log(height);
    document.getElementById('result').innerHTML = `<h4>Lượng calo tiêu thụ hàng ngày là: ${calo} calories.</h4> 
    <h4>Lượng calo giảm cân bạn cần là: ${calogiam} calories.</h4> 
    <h4>Lượng calo tăng cân bạn cần là : ${calotang} calories.</h4>`;
    console.log('click')
});