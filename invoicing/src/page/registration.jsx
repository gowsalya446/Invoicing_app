import "./registration.css"
import { Formik, Form, Field } from 'formik';
import * as Yup from 'yup';
import { useNavigate } from "react-router-dom";

const SignupSchema = Yup.object().shape({
  name: Yup.string()
    .required("Name is required")
    .min(2, "Too Short!'")
    .max(14, "Maximum length of name should not exceed 14 characters"),
  email: Yup.string()
    .required("Email is required")
    .email('Invalid Email'),
  phone: Yup.string()
    .required("Phone number is required")
    .matches(/^\d{10}$/, "Phone Number should be exactly 10 digits"),
  password: Yup.string()
    .required("Password is required")
    .min(6, "Too Short Password!'")
    .max(16, "Too Long Password!")       
});


function Registraion() {
   
const navigate=useNavigate();
  function Submit(value) {
  
    navigate('/message', true);
  }

  return (
    <div>
      <div>
        <h3 className="head">Register Page</h3>
      </div>
      <Formik
        initialValues={{ name: '', email: '', phone: '', password: '' }}
        validationSchema={SignupSchema}
        onSubmit={ Submit}
      >
        {({ errors, touched }) => (
          <Form className="form">
            <div className="reg">
              <div className="field">
                <label>Name</label>
                <Field name='name' className='input' type="text" />
                {errors.name && touched.name ? (
                  <div className='err'>{errors.name}</div>
                ) : null}
              </div>
              <div className="field">
                <label>Email Address</label>
                <Field name="email" className='input' type="email" />
                {errors.email && touched.email ? (
                  <div className='err'>{errors.email}</div>
                ) : null}
              </div>
              <div className="field">
                <label>Phone number</label>
                <Field name="phone" className='input' type="number" />
                {errors.phone && touched.phone ? (
                  <div className='err'>{errors.phone}</div>
                ) : null}
              </div>
              <div className="field">
                <label>Password</label>
                <Field name="password" className='input' type="password" />
                {errors.password && touched.password ? (
                  <div className='err'>{errors.password}</div>
                ) : null}
              </div>

              <button type="submit" className="btn btn-primary">Submit</button>
              <div className="login">Already have login?<a href="/login">Click here</a></div>
            </div> 
          </Form>
        )}
      </Formik>    
    </div>
  );
}

export default Registraion;
