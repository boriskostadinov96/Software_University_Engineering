function calculateCommission(city, sales) {
    if (sales < 0 || !["Sofia", "Varna", "Plovdiv"].includes(city)) {
        console.log("error");
        return;
    }

    let commissionRate;


    if (city === "Sofia") {
        if (sales <= 500) commissionRate = 0.05;
        else if (sales <= 1000) commissionRate = 0.07;
        else if (sales <= 10000) commissionRate = 0.08;
        else commissionRate = 0.12;
    
    } else if (city === "Varna") {
        if (sales <= 500) commissionRate = 0.045;
        else if (sales <= 1000) commissionRate = 0.075;
        else if (sales <= 10000) commissionRate = 0.10;
        else commissionRate = 0.13;
    
    } else if (city === "Plovdiv") {
        if (sales <= 500) commissionRate = 0.055;
        else if (sales <= 1000) commissionRate = 0.08;
        else if (sales <= 10000) commissionRate = 0.12;
        else commissionRate = 0.145;
    }

    let commission = sales * commissionRate;
    console.log(commission.toFixed(2));
}


calculateCommission("Sofia", 1500); 