var mysql      = require('mysql');
var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  password : 'dhkswjsdjdl1!',
  database : 'fintech',
  port: "3307"
});
 
connection.connect();
 
connection.query('SELECT * FROM fintech.user', function (error, results, fields) {
  if (error) throw error;
  sqlResult=results;
  for(var i=0; i<results.length; i++){
    console.log(results[0]);
  }
});
 
connection.end();