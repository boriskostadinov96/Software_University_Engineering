function repaint(nylon, paint, liquid, hours) {
    let totalNylon = nylon + 2;
    let totalPaint = paint + (paint * 0.10);
    
    let nylonCost = totalNylon * 1.5;
    let paintCost = totalPaint * 14.5;
    let liquidCost = liquid * 5;
    let bagsCost = 0.40;

    let totalMaterialCost = nylonCost + paintCost + liquidCost + bagsCost;
    
    let workersCost = (totalMaterialCost * 0.30) * hours;
    
    let totalCost = totalMaterialCost + workersCost;
    

    console.log(totalCost);
}

repaint(10,
    11,
    4 ,
    8
    )