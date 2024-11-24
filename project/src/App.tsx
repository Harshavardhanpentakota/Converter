import './App.css'
import Navbar from './components/Navbar'
import Footer from './components/Footer'
import { Tabs, TabsContent, TabsList, TabsTrigger } from "./components/ui/tabs"
import ImageGenerator from './components/imageGenerator'
import VideoGenerator from './components/videoGenerator'
import InstructionFollower from './components/instructionFollower'

function App() {

  return (
    <div className='bg-black'>
      <Navbar/>
      <div className='m-5'>
      <h1 className="scroll-m-20 text-center text-4xl text-white font-extrabold tracking-tight lg:text-5xl">
        Convert Anything to Anything
      </h1>
      <div className=' flex justify-center items-center my-5' >
      <Tabs defaultValue="account" className="w-full bg-black text-white p-5 flex flex-col border-gray-500 border-2 rounded-lg">
        <TabsList className='bg-custom_1 gap-5'>
         <TabsTrigger value="ImageGenerator">Image Generator</TabsTrigger>
         <TabsTrigger value="VideoGenerator">Video Generator</TabsTrigger>
         <TabsTrigger value="Instruction">Instruction Follower</TabsTrigger>
        </TabsList>
        <TabsContent value="ImageGenerator"><ImageGenerator/></TabsContent>
        <TabsContent value="VideoGenerator"><VideoGenerator/></TabsContent>
        <TabsContent value="Instruction"><InstructionFollower/></TabsContent>
      </Tabs>
      </div>
      </div>
      <Footer/>
    </div>
  )
}

export default App
