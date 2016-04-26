//
//  Patient.swift
//  hospitalist
//
//  Created by Aana Bansal on 4/18/16.
//  Copyright © 2016 Aana Bansal. All rights reserved.
//

import UIKit

class Patient{
    // MARK: Properties
    
    var name: String
    var index: Int
    
    //MARK: Initialization 
    
    init?(name: String, index: Int){
        self.name = name
        self.index = index
        
        //Initialization should fail if name is empty or index is less than 0
        if name.isEmpty || index < 0 {
            return nil
        }
    }
}
