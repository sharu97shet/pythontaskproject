+import React, { useState } from "react";
import { useEffect } from "react";
import axios from "axios";
import {Button,ButtonToolbar} from 'react-bootstrap';

import {AddDepModal} from './AddDepModal';
import {EditDepModal} from './EditDepModal';
// import 'bootstrap/dist/css/bootstrap.css';
// import 'bootstrap/dist/css/bootstrap.min.css';

/*
function Department()
{
    
 const[model,showmodel]=useState(false)

 
 const [id, depid] = useState([]);

 const [dep, depname] = useState([]);

 const[close , closemodel]=useState(false)

 const[editmodel , editclosemodel]=useState(false)

 let editModalClose=()=>this.setState({editModalShow:false});

 const [name, showname] = useState();
 const {deps, setid,setdepname}='';

  // axios.get('http://127.0.0.1:8000/empapi/department').then(function(result){

  // console.log(result.data)
  //      }
  // )

 let depdata={dep:[]}

  useEffect( ()=>{
   getdapartments()
  } ,[] )

  let getdapartments= async()=>{

    let response= await axios.get('http://127.0.0.1:8000/empapi/department');
    let data= await response.data;
    console.log('data', data)
     depname(data)

  }

  function modeldisplay()
    {
      alert("p")
      showmodel(true)
      
    }

    function editdisplay()
    {

      alert('a')
      showname()
      //alert("pwwwww")
      editclosemodel(true)
      
    }

    function editmodelclose()
    {
      //alert("pwwwww")
      editclosemodel(false)
      
    }

    function handleCloseModal  () {

      alert("hiiii")
      closemodel(false)
     }

/*
  useEffect(() => {
    fetch(
      'http://127.0.0.1:8000/empapi/department'
    )
      .then((res) => res.json())
      .then((data) => {
        // console.log("exec");
       // updep(data);
       depdata.dep=data;
        console.log(depdata);
      })
      .catch((err) => {
        console.log("Err");
        console.log(err);
      });
  });
*/

   if (dep.length>0) {

     return (
            <div className="conatiner">

      <p>container</p>


      {/* onClick={()=>this.setState({addModalShow:true})}> */}

      <ButtonToolbar>
                  <Button className='primary' variant='primary'
                    onClick={modeldisplay}>
                    Add Department</Button>

                    { <AddDepModal  show={model}  />
                    }
                </ButtonToolbar>

             {/* <AddDepModal show /> */}

            <strong>{}</strong> 

       <div className="container mt-4">
            <div className="row">
              <div className="col">
                <table className="table table-bordered table-hover">
                <thead>
                    <tr>
                      <th>Id</th>
                      <th>Name</th>
                      <th>Action</th>
                      
                    </tr>
                  </thead>

                  <tbody> 
        {dep.map((details,index) => {

          return(

          <tr key={details.DepartmentId}  >

            <td  >{details.DepartmentId}</td>
            <td>{details.DepartmentName}</td>
             <td ><ButtonToolbar>
    <Button className="mr-2" variant="info" 
      onClick={ editdisplay() }  
       >    Edit
      </Button>

    
   
   <EditDepModal show={editmodel}
        onHide={editmodelclose}   
         depid={index}   
         showname(details.DepartmentName)
         />

        {/* <Button className="mr-2" variant="danger"
    onClick={()=>this.deleteDep(dep.DepartmentId)}>
            Delete
        </Button>

        

        <EditDepModal show={this.state.editModalShow}
        onHide={editclosemodel}
        depid={depid}
        depname={depname}/> */  }


</ButtonToolbar>




</td> 

            </tr>

                )

      })}

</tbody>

                </table>
                  </div>
                  </div>
                  </div>

         
  </div>

  );
}
}




 export default Department;

