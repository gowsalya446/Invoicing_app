import "./login.css"
import { Formik, Form, Field } from 'formik';
import * as Yup from 'yup';
import { useNavigate } from "react-router-dom";


const SignupSchema = Yup.object().shape({
  email: Yup.string()
    .required("Email is required")
    .email('Invalid Email'),
  
  password: Yup.string()
    .required("Password is required")
    .min(6, "Too Short Password!'")
    .max(16, "Too Long Password!")       
});
function Login(){
  const navigate=useNavigate();
  function Submit(value) {
  
    navigate('/');
  }

    return(
      <Formik
        initialValues={{ email:'', password:'' }}
        validationSchema={SignupSchema}
        onSubmit={ Submit}
      >
         {({ errors, touched }) => (
        <Form className="form-lo">
  <div className="mb-3">
    <label for="exampleInputEmail1" className="form-label label">Email address</label>
    <Field name='email' type="email" className="form-control wid" id="exampleInputEmail1" aria-describedby="emailHelp"/>
    {errors.email && touched.email ? (
                  <div className='err'>{errors.email}</div>
                ) : null}
  </div>
  <div className="mb-3">
    <label for="exampleInputPassword1" className="form-label label">Password</label>
    <Field name='password' type="password" className="form-control wid" id="exampleInputPassword1"/>
    
                {errors.password && touched.password ? (
                  <div className='err'>{errors.password}</div>
                ) : null}
  </div>
  
  <button type="submit" className="btn btn-primary">Login</button>

  <div className='signin'>No account for you?<a href='./register'>click here</a></div>
</Form>
 )}
</Formik>
        );
    }
    
    export default Login;
