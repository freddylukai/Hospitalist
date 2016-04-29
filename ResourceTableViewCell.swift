//
//  ResourceTableViewCell.swift
//  hospitalist
//
//  Created by Aana Bansal on 4/26/16.
//  Copyright © 2016 Aana Bansal. All rights reserved.
//

import UIKit

class ResourceTableViewCell: UITableViewCell {
    
    // MARK: Properties
    @IBOutlet weak var nameLabel: UILabel!
    @IBOutlet weak var availibilityLabel: UILabel!
    @IBOutlet weak var totalLabel: UILabel!
    
    override func awakeFromNib() {
        super.awakeFromNib()
        // Initialization code
    }

    override func setSelected(selected: Bool, animated: Bool) {
        super.setSelected(selected, animated: animated)

        // Configure the view for the selected state
    }

}
