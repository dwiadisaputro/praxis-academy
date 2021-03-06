import { LockOutlined, UserOutlined } from '@ant-design/icons';
import { Button, Checkbox, Form, Input, Card } from 'antd';
import "./Login.css"

const Login = () => {
  const onFinish = (values) => {
    console.log('Received values of form: ', values);
  };

  return (
    <div className='login'>
        {/* <Card style={{width: "400px", height: "300px", justifyContent:"center"}}> */}
        <Card className='card'>
        <Form className='ard' name="normal_login" initialValues={{
            remember: true,
        }} onFinish={onFinish} >

            <h1>Login</h1>

        <Form.Item name="username" rules={[
            {
                required: true,
                message: 'Please input your Username!',
            },
            ]}
        >
            <Input prefix={<UserOutlined className="site-form-item-icon" />} placeholder="Username" />
        </Form.Item>
        <Form.Item name="password" rules={[
            {
                required: true,
                message: 'Please input your Password!',
            },
            ]}
        >
            <Input prefix={<LockOutlined className="site-form-item-icon" />}
            type="password" placeholder="Password" />
        </Form.Item>
        <Form.Item>
            <Form.Item name="remember" valuePropName="checked" noStyle>
            <Checkbox>Remember me</Checkbox>
            </Form.Item>

            <a className="login-form-forgot" href="/lupasandi">
            Forgot password
            </a>
        </Form.Item>

        <Form.Item>
            <Button type="primary" htmlType="submit" className="login-form-button">
            Log in
            </Button> &nbsp;
            Or &nbsp; <a href="/registrasion">register now!</a>
        </Form.Item>
        </Form>
        </Card>
    </div> 
  );
};

export default Login;
