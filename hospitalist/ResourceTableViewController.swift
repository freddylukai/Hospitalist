//
//  ResouceTableViewController.swift
//  hospitalist
//
//  Created by Aana Bansal on 4/18/16.
//  Copyright © 2016 Aana Bansal. All rights reserved.
//

import UIKit
import Freddy

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
            print("here we are")
            
            var optData:NSData? = nil
            do {
                optData = try NSData(contentsOfURL: URL!, options: NSDataReadingOptions())
            }
            catch {
                print("Handle \(error) here")
            }
            print("what about here")
            if let data = optData {
                print("here i am")
                let myj = try JSON(data: data)
                print("did we get this far")
                print(myj)
                let jres = try myj.array("resources")
                for (index, v) in jres.enumerate() {
                    print("index = " + String(index))
                    print("v = " + String(v))
                    let nam = try v.string("name")
                    print("name : "+nam)
                    let tot = Int(try v.string("total"))
                    print("tot : "+String(tot))
                    let ava = Int(try v.string("available"))
                    print("ava : "+String(ava))

                    let cur = Resource(name: nam, total: tot!, available: ava!)
                    resources.append(cur!)
                }
            }
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
