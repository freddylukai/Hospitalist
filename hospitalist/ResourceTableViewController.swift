//
//  ResouceTableViewController.swift
//  hospitalist
//
//  Created by Aana Bansal on 4/18/16.
//  Copyright © 2016 Aana Bansal. All rights reserved.
//

import UIKit

class ResourceTableViewController: UITableViewController {
    
    // MARK: Properties
    
    var resources = [Resource]()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        //read from database
        loadResources()
    }
    
    
    func loadResources(){
        let URL = NSURL(string: "http://ec2-52-90-89-173.compute-1.amazonaws.com/resourceview/")
        
        do {
            let htmlSource = try NSString(contentsOfURL: URL!, encoding: NSUTF8StringEncoding)
            var foo = htmlSource.componentsSeparatedByString("\"")
            
            print(foo)
            var name1 = foo[5]
            var total1 = Int(foo[9])
            var available1 = Int(foo[13])
            let resource1 = Resource(name: name1, total: total1!, available: available1!)
            resources.append(resource1!)
            
            var name2 = foo[29]
            var total2 = Int(foo[33])
            var available2 = Int(foo[37])
            let resource2 = Resource(name: name2, total: total2!, available: available2!)
            resources.append(resource2!)
            
            var name3 = foo[41]
            var total3 = Int(foo[45])
            var available3 = Int(foo[49])
            let resource3 = Resource(name: name3, total: total3!, available: available3!)
            resources.append(resource3!)
        }
            
        catch let error as NSError{
            print ("ERROR: \(error)")
        }
        
        
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    // MARK: - Table view data source
    
    override func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        
        return 1
    }
    
    override func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        
        return resources.count
    }
    
    override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        // Table view cells are reused and should be dequeued using a cell identifier.
        let cellIdentifier = "ResourceTableViewCell"
        let cell = tableView.dequeueReusableCellWithIdentifier(cellIdentifier, forIndexPath: indexPath) as! ResourceTableViewCell
        
        // Fetches the appropriate meal for the data source layout.
        let resource = resources[indexPath.row]
        print(resource.name)
        cell.nameLabel.text = resource.name
        cell.totalLabel.text = String(resource.total)
        cell.availibilityLabel.text = String(resource.available)
        
        return cell
    }
    
        
}
