import { useState, useEffect, useRef } from "react";
import { useAuth } from "@/lib/auth";
import { useLocation } from "wouter";
import { useToast } from "@/hooks/use-toast";
import { Eye, EyeOff, LogIn, UserPlus } from "lucide-react";
import icaLogo from "@assets/ica-logo_1772293580977.jpg";

export default function LoginPage() {
  const [loginForm, setLoginForm] = useState({ username: "", password: "" });
  const [signupForm, setSignupForm] = useState({ fullName: "", email: "", mobile: "", username: "", password: "" });
  const [showPassword, setShowPassword] = useState(false);
  const [loading, setLoading] = useState(false);
  const [deactivated, setDeactivated] = useState(false);
  const [signupLoading, setSignupLoading] = useState(false);
  const [activeTab, setActiveTab] = useState<"login" | "signup">("login");
  const { login } = useAuth();
  const [, setLocation] = useLocation();
  const { toast } = useToast();

  const canvasRef = useRef<HTMLCanvasElement>(null);
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;
    let animId: number;
    type Line = { x1: number; y1: number; x2: number; y2: number; pulse: number; speed: number };
    let lines: Line[] = [];
    const buildLines = () => {
      const W = canvas.width, H = canvas.height;
      lines = Array.from({ length: 45 }, () => {
        const horiz = Math.random() > 0.5;
        const x1 = Math.random() * W;
        const y1 = Math.random() * H;
        const len = 80 + Math.random() * 200;
        return {
          x1, y1,
          x2: horiz ? x1 + len : x1,
          y2: horiz ? y1 : y1 + len,
          pulse: Math.random(),
          speed: 0.003 + Math.random() * 0.007,
        };
      });
    };
    const resize = () => {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
      buildLines();
    };
    resize();
    window.addEventListener("resize", resize);
    const draw = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      lines.forEach((l) => {
        ctx.beginPath();
        ctx.moveTo(l.x1, l.y1);
        ctx.lineTo(l.x2, l.y2);
        ctx.strokeStyle = "rgba(46,117,182,0.2)";
        ctx.lineWidth = 0.8;
        ctx.stroke();
        ctx.beginPath();
        ctx.arc(l.x1, l.y1, 2, 0, Math.PI * 2);
        ctx.fillStyle = "rgba(46,117,182,0.45)";
        ctx.fill();
        ctx.beginPath();
        ctx.arc(l.x2, l.y2, 2, 0, Math.PI * 2);
        ctx.fillStyle = "rgba(46,117,182,0.45)";
        ctx.fill();
        const px = l.x1 + (l.x2 - l.x1) * l.pulse;
        const py = l.y1 + (l.y2 - l.y1) * l.pulse;
        const trail = 8;
        for (let t = trail; t >= 1; t--) {
          const tp = Math.max(0, l.pulse - t * 0.035);
          const tx = l.x1 + (l.x2 - l.x1) * tp;
          const ty = l.y1 + (l.y2 - l.y1) * tp;
          ctx.beginPath();
          ctx.arc(tx, ty, 1.5, 0, Math.PI * 2);
          ctx.fillStyle = "rgba(96,165,250," + (0.15 * (trail - t) / trail) + ")";
          ctx.fill();
        }
        ctx.beginPath();
        ctx.arc(px, py, 3, 0, Math.PI * 2);
        ctx.fillStyle = "rgba(96,165,250,1)";
        ctx.fill();
        l.pulse += l.speed;
        if (l.pulse > 1) l.pulse = 0;
      });
      animId = requestAnimationFrame(draw);
    };
    draw();
    return () => {
      cancelAnimationFrame(animId);
      window.removeEventListener("resize", resize);
    };
  }, []);


  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    if (loading) return;
    setLoading(true);
    try {
      await login(loginForm.username, loginForm.password);
      setTimeout(() => setLocation("/"), 100);
    } catch (err: any) {
      if (err.message?.includes("deactivated") || err.message?.includes("inactive")) {
        setDeactivated(true);
      } else {
        toast({ title: "Login Failed", description: err.message, variant: "destructive" });
      }
      setLoading(false);
    }
  };

  const handleSignup = async (e: React.FormEvent) => {
    e.preventDefault();
    if (signupLoading) return;
    setSignupLoading(true);
    try {
      const res = await fetch("/api/auth/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(signupForm),
      });
      const data = await res.json();
      if (!data.success) throw new Error(data.message);
      toast({ title: "Registration Successful", description: data.message });
      setSignupForm({ fullName: "", email: "", mobile: "", username: "", password: "" });
    } catch (err: any) {
      toast({ title: "Registration Failed", description: err.message, variant: "destructive" });
    } finally {
      setSignupLoading(false);
    }
  };

  return (
    <div style={{minHeight:"100vh",display:"flex",background:"#050d1a",fontFamily:"'Segoe UI',system-ui,sans-serif",position:"relative",overflow:"hidden"}}>
      <style>{`
        @keyframes float1{0%,100%{transform:translate(0,0) scale(1)}50%{transform:translate(30px,-20px) scale(1.05)}}
        @keyframes float2{0%,100%{transform:translate(0,0) scale(1)}50%{transform:translate(-25px,30px) scale(0.97)}}
        @keyframes float3{0%,100%{transform:translate(0,0)}50%{transform:translate(20px,25px)}}
        @keyframes fadeUp{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:translateY(0)}}
        @keyframes pulse-ring{0%{transform:scale(0.95);opacity:0.7}50%{transform:scale(1.05);opacity:0.3}100%{transform:scale(0.95);opacity:0.7}}
        @keyframes spin{to{transform:rotate(360deg)}}
        .login-input{width:100%;padding:12px 16px;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);border-radius:10px;color:#fff;font-size:14px;outline:none;transition:all 0.2s;box-sizing:border-box;}
        .login-input::placeholder{color:rgba(255,255,255,0.3);}
        .login-input:focus{border-color:rgba(59,130,246,0.6);background:rgba(255,255,255,0.08);box-shadow:0 0 0 3px rgba(59,130,246,0.15);}
        .login-label{display:block;font-size:12px;font-weight:600;color:rgba(255,255,255,0.5);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:8px;}
        .tab-btn{flex:1;padding:10px;border:none;background:transparent;color:rgba(255,255,255,0.4);font-size:14px;font-weight:600;cursor:pointer;border-radius:8px;transition:all 0.2s;}
        .tab-btn.active{background:rgba(59,130,246,0.2);color:#60a5fa;}
        .tab-btn:hover:not(.active){color:rgba(255,255,255,0.7);}
        .submit-btn{width:100%;padding:13px;border:none;border-radius:10px;font-size:14px;font-weight:700;cursor:pointer;letter-spacing:0.03em;transition:all 0.2s;display:flex;align-items:center;justify-content:center;gap:8px;background:linear-gradient(135deg,#1d4ed8,#2563eb,#3b82f6);color:white;box-shadow:0 4px 20px rgba(37,99,235,0.4);}
        .submit-btn:hover:not(:disabled){transform:translateY(-1px);box-shadow:0 6px 25px rgba(37,99,235,0.55);}
        .submit-btn:disabled{opacity:0.6;cursor:not-allowed;}
        .feature-card{background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);border-radius:12px;padding:16px;transition:all 0.3s;}
        .feature-card:hover{background:rgba(255,255,255,0.07);border-color:rgba(59,130,246,0.3);transform:translateY(-2px);}
        .spin{width:16px;height:16px;border:2px solid rgba(255,255,255,0.3);border-top-color:white;border-radius:50%;animation:spin 0.7s linear infinite;}
        @media(min-width:1024px){.mobile-logo{display:none!important}.left-panel{display:flex!important}.divider{display:block!important}}
      `}</style>

      <div style={{position:"absolute",inset:0,overflow:"hidden",pointerEvents:"none"}}>
        <div style={{position:"absolute",top:"-15%",left:"-10%",width:"600px",height:"600px",borderRadius:"50%",background:"radial-gradient(circle,rgba(29,78,216,0.18) 0%,transparent 70%)",animation:"float1 8s ease-in-out infinite"}}/>
        <div style={{position:"absolute",bottom:"-20%",right:"-10%",width:"700px",height:"700px",borderRadius:"50%",background:"radial-gradient(circle,rgba(37,99,235,0.12) 0%,transparent 70%)",animation:"float2 10s ease-in-out infinite"}}/>
        <div style={{position:"absolute",top:"40%",left:"40%",width:"400px",height:"400px",borderRadius:"50%",background:"radial-gradient(circle,rgba(6,182,212,0.07) 0%,transparent 70%)",animation:"float3 7s ease-in-out infinite"}}/>
        <svg style={{position:"absolute",inset:0,width:"100%",height:"100%",opacity:0.04}}>
          <defs><pattern id="grid" width="60" height="60" patternUnits="userSpaceOnUse"><path d="M 60 0 L 0 0 0 60" fill="none" stroke="rgba(255,255,255,0.8)" strokeWidth="0.5"/></pattern></defs>
          <rect width="100%" height="100%" fill="url(#grid)"/>
        </svg>
        <canvas
          ref={canvasRef}
          style={{ position: "absolute", inset: 0, width: "100%", height: "100%", pointerEvents: "none" }}
        />
      </div>

      <div className="left-panel" style={{display:"none",width:"52%",flexDirection:"column",justifyContent:"center",alignItems:"center",padding:"60px",position:"relative"}}>
        <div style={{maxWidth:"440px",width:"100%",animation:"fadeUp 0.8s ease forwards"}}>
          <div style={{display:"flex",alignItems:"center",gap:"16px",marginBottom:"48px"}}>
            <div style={{position:"relative"}}>
              <div style={{position:"absolute",inset:"-6px",borderRadius:"20px",background:"linear-gradient(135deg,#1d4ed8,#06b6d4)",opacity:0.4,animation:"pulse-ring 3s ease-in-out infinite"}}/>
              <img src={icaLogo} alt="ICA" style={{width:"64px",height:"64px",borderRadius:"16px",objectFit:"cover",position:"relative",boxShadow:"0 8px 32px rgba(0,0,0,0.4)"}} data-testid="img-ica-logo-hero"/>
            </div>
            <div>
              <h1 style={{margin:0,fontSize:"26px",fontWeight:800,color:"#fff",letterSpacing:"-0.02em"}}>ICA CRM</h1>
              <p style={{margin:0,fontSize:"13px",color:"#60a5fa",fontWeight:500}}>Innovation, Consulting & Automation</p>
            </div>
          </div>
          <div style={{marginBottom:"40px"}}>
            <h2 style={{margin:"0 0 12px",fontSize:"38px",fontWeight:800,color:"#fff",lineHeight:1.15,letterSpacing:"-0.03em"}}>
              Manage Leads.<br/>
              <span style={{background:"linear-gradient(135deg,#3b82f6,#06b6d4)",WebkitBackgroundClip:"text",WebkitTextFillColor:"transparent"}}>Grow Faster.</span>
            </h2>
            <p style={{margin:0,fontSize:"15px",color:"rgba(255,255,255,0.45)",lineHeight:1.7}}>AI-powered insurance CRM with smart meeting analysis, RC lookup, and multi-tier team management.</p>
          </div>
          <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:"12px"}}>
            {[{icon:"🧠",title:"AI Proceeding",desc:"Smart meeting analysis"},{icon:"📊",title:"KPI Engine",desc:"Performance tracking"},{icon:"👥",title:"Team Management",desc:"Multi-tier hierarchy"},{icon:"🔐",title:"Enterprise Security",desc:"Role-based access"}].map((f,i)=>(
              <div key={i} className="feature-card">
                <div style={{fontSize:"22px",marginBottom:"8px"}}>{f.icon}</div>
                <p style={{margin:"0 0 4px",fontSize:"13px",fontWeight:700,color:"rgba(255,255,255,0.9)"}}>{f.title}</p>
                <p style={{margin:0,fontSize:"11px",color:"rgba(255,255,255,0.35)"}}>{f.desc}</p>
              </div>
            ))}
          </div>
          <div style={{marginTop:"32px",display:"flex",gap:"32px",padding:"20px 24px",background:"rgba(255,255,255,0.04)",borderRadius:"12px",border:"1px solid rgba(255,255,255,0.07)"}}>
            {[["AI","Powered"],["Multi","Tenant"],["100%","Cloud"]].map(([val,label],i)=>(
              <div key={i}>
                <p style={{margin:0,fontSize:"22px",fontWeight:800,color:"#60a5fa"}}>{val}</p>
                <p style={{margin:0,fontSize:"11px",color:"rgba(255,255,255,0.35)",marginTop:"2px"}}>{label}</p>
              </div>
            ))}
          </div>
        </div>
      </div>

      <div className="divider" style={{display:"none",width:"1px",background:"linear-gradient(to bottom,transparent,rgba(255,255,255,0.08),transparent)",flexShrink:0}}/>

      <div style={{flex:1,display:"flex",alignItems:"center",justifyContent:"center",padding:"32px 24px"}}>
        <div style={{width:"100%",maxWidth:"400px",animation:"fadeUp 0.8s ease 0.2s both"}}>
          <div className="mobile-logo" style={{textAlign:"center",marginBottom:"32px"}}>
            <img src={icaLogo} alt="ICA" style={{width:"56px",height:"56px",borderRadius:"14px",objectFit:"cover",marginBottom:"12px"}} data-testid="img-ica-logo"/>
            <p style={{margin:0,fontSize:"13px",color:"rgba(255,255,255,0.4)",fontWeight:500}} data-testid="text-tagline-mobile">Innovation, Consulting & Automation</p>
          </div>
          <div style={{background:"rgba(255,255,255,0.04)",backdropFilter:"blur(20px)",border:"1px solid rgba(255,255,255,0.09)",borderRadius:"20px",padding:"32px",boxShadow:"0 25px 60px rgba(0,0,0,0.5)"}}>
            <div style={{marginBottom:"24px"}}>
              <h2 style={{margin:"0 0 4px",fontSize:"22px",fontWeight:800,color:"#fff",letterSpacing:"-0.02em"}}>Welcome Back</h2>
              <p style={{margin:0,fontSize:"13px",color:"rgba(255,255,255,0.35)"}}>Sign in to your account or create a new one</p>
            </div>
            <div style={{display:"flex",background:"rgba(0,0,0,0.3)",borderRadius:"10px",padding:"4px",marginBottom:"24px",gap:"4px"}}>
              <button className={`tab-btn${activeTab==="login"?" active":""}`} onClick={()=>setActiveTab("login")} data-testid="tab-login">Sign In</button>
              <button className={`tab-btn${activeTab==="signup"?" active":""}`} onClick={()=>setActiveTab("signup")} data-testid="tab-signup">Sign Up</button>
            </div>
            {deactivated ? (
              <div style={{textAlign:"center",padding:"8px 0"}}>
                <div style={{width:"56px",height:"56px",borderRadius:"50%",background:"rgba(239,68,68,0.15)",display:"flex",alignItems:"center",justifyContent:"center",margin:"0 auto 16px"}}>
                  <span style={{fontSize:"28px"}}>🔴</span>
                </div>
                <h3 style={{margin:"0 0 8px",fontSize:"18px",fontWeight:700,color:"#fff"}}>Subscription Expired</h3>
                <p style={{margin:"0 0 20px",fontSize:"13px",color:"rgba(255,255,255,0.5)",lineHeight:1.6}}>Your agency subscription has expired. Renew now to restore access for your entire team.</p>
                <a href="https://icaweb.in/#pricing" target="_blank" rel="noopener noreferrer"
                  style={{display:"block",width:"100%",padding:"13px",borderRadius:"10px",background:"linear-gradient(135deg,#dc2626,#ef4444)",color:"#fff",fontWeight:700,fontSize:"14px",textDecoration:"none",textAlign:"center",marginBottom:"12px",boxSizing:"border-box"}}>
                  🔄 Renew Subscription Now
                </a>
                <a href="https://wa.me/919967969850?text=Hi+Sameer%2C+my+agency+subscription+expired.+Please+help+me+renew."
                  target="_blank" rel="noopener noreferrer"
                  style={{display:"block",width:"100%",padding:"11px",borderRadius:"10px",background:"rgba(37,211,102,0.15)",border:"1px solid rgba(37,211,102,0.3)",color:"#25d366",fontWeight:600,fontSize:"13px",textDecoration:"none",textAlign:"center",marginBottom:"16px",boxSizing:"border-box"}}>
                  📲 WhatsApp Sameer to Renew
                </a>
                <button onClick={()=>setDeactivated(false)} style={{background:"none",border:"none",color:"rgba(255,255,255,0.35)",fontSize:"12px",cursor:"pointer",textDecoration:"underline"}}>
                  ← Back to Login
                </button>
              </div>
            ) : activeTab==="login" ? (
              <form onSubmit={handleLogin} style={{display:"flex",flexDirection:"column",gap:"16px"}}>
                <div>
                  <label className="login-label">Username</label>
                  <input className="login-input" data-testid="input-username" placeholder="Enter your username" value={loginForm.username} onChange={(e)=>setLoginForm({...loginForm,username:e.target.value})} required autoFocus/>
                </div>
                <div>
                  <label className="login-label">Password</label>
                  <div style={{position:"relative"}}>
                    <input className="login-input" data-testid="input-password" type={showPassword?"text":"password"} placeholder="Enter your password" value={loginForm.password} onChange={(e)=>setLoginForm({...loginForm,password:e.target.value})} style={{paddingRight:"44px"}} required/>
                    <button type="button" onClick={()=>setShowPassword(!showPassword)} data-testid="button-toggle-password" style={{position:"absolute",right:"12px",top:"50%",transform:"translateY(-50%)",background:"none",border:"none",cursor:"pointer",color:"rgba(255,255,255,0.35)",padding:"4px",display:"flex",alignItems:"center"}}>
                      {showPassword?<EyeOff size={16}/>:<Eye size={16}/>}
                    </button>
                  </div>
                </div>
                <button type="submit" className="submit-btn" disabled={loading} data-testid="button-login" style={{marginTop:"4px"}}>
                  {loading?<><div className="spin"/>Signing in...</>:<><LogIn size={16}/>Sign In</>}
                </button>
              </form>
            ) : null}
            {!deactivated && activeTab==="signup"&&(
              <form onSubmit={handleSignup} style={{display:"flex",flexDirection:"column",gap:"14px"}}>
                {[{label:"Full Name",key:"fullName",type:"text",placeholder:"Enter your full name",testid:"input-signup-name"},{label:"Email",key:"email",type:"email",placeholder:"Enter your email",testid:"input-signup-email"},{label:"Mobile Number",key:"mobile",type:"tel",placeholder:"Enter your mobile number",testid:"input-signup-mobile",minLength:10},{label:"Username",key:"username",type:"text",placeholder:"Choose a username",testid:"input-signup-username"},{label:"Password",key:"password",type:"password",placeholder:"Choose a password (min 6 chars)",testid:"input-signup-password",minLength:6}].map(({label,key,type,placeholder,testid,minLength})=>(
                  <div key={key}>
                    <label className="login-label">{label}</label>
                    <input className="login-input" data-testid={testid} type={type} placeholder={placeholder} value={(signupForm as any)[key]} onChange={(e)=>setSignupForm({...signupForm,[key]:e.target.value})} required minLength={minLength}/>
                  </div>
                ))}
                <button type="submit" className="submit-btn" disabled={signupLoading} data-testid="button-signup" style={{marginTop:"4px"}}>
                  {signupLoading?<><div className="spin"/>Registering...</>:<><UserPlus size={16}/>Sign Up</>}
                </button>
                <p style={{margin:0,fontSize:"11px",color:"rgba(255,255,255,0.25)",textAlign:"center",lineHeight:1.6}}>Your account will require admin approval before you can login.</p>
              </form>
            )}
          </div>
          <div style={{textAlign:"center",marginTop:"24px"}} data-testid="text-footer">
            <p style={{margin:"0 0 4px",fontSize:"12px",fontWeight:600,color:"rgba(255,255,255,0.25)",letterSpacing:"0.05em"}}>ICA — Innovation, Consulting & Automation</p>
            <p style={{margin:0,fontSize:"12px",color:"rgba(255,255,255,0.2)"}}>Support: +91 99679 69850</p>
          </div>
        </div>
      </div>
    </div>
  );
}
