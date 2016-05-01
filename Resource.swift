//
//  Resource.swift
//  hospitalist
//
//  Created by Aana Bansal on 4/18/16.
//  Copyright © 2016 Aana Bansal. All rights reserved.
//

import UIKit


class Resource{
    // MARK: Properties
    var name: String
    var total: Int
    var available: Int
    
    //MARK: Initialization
    
    init?(name: String, total: Int, available: Int){
        self.name = name
        self.total = total
        self.available = available
    }
}