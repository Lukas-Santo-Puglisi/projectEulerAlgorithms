// Task: Write a React functional component named UserProfile using the ES6 arrow function syntax. The component should display a user's name and email in a styled <div> element. The component should accept name and email as props. Additionally, demonstrate how to use this component in a simple React application.

const UserProfile = ({userName, userEmail}) =>{
  return <div style={{color:'red'}}> 
    <p>
    {userName}
    </p>
    <p>
    {userEmail}
    </p>
  
  </div>
}