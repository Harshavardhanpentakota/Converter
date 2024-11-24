import Navbar from './components/Navbar';
import './App.css';
import Footer from './components/Footer';

function App() {
  return (
   <div className='bg-slate-300'>
    <Navbar/>
    <div className='m-5'>
      <p className='text-center font-semibold text-5xl'>Convert Anything to Anything</p>
    </div>
    <Footer/>
   </div>
  );
}

export default App;
