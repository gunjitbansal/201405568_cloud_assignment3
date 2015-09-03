from mininet.topo import Topo

class MyTopo( Topo ):

	def __init__(self):

		Topo.__init__(self)

		x=input('no of switch ')
		y=input('no of host per switch ')

		print x,y
		
		ss='s'
		s=[]
		for i in range(1,x+1):
			t=ss+str(i)
			s.append(t)

		hs='h'
		h=[]
		for i in range(1,(y*x)+1):
			t=hs+str(i)
			h.append(t)
	
		print s
		print h

		hl=[]
		j=1
		k=1
		counter=1
		ip_even='10.0.0.'
		ip_odd='11.0.0.'

		for i in h:	
			if counter%2==0 :
				qq="\'"+ip_even+str(j)+"\'"
				print qq
				a=self.addHost(i,ip=qq)
				j=j+1
			else:
				qq="\'"+ip_odd+str(k)+"\'"
				print qq
				a=self.addHost(i,ip=qq)
				k=k+1
			hl.append(a)
			counter=counter+1

		sl=[]
		for i in s:
			a=self.addSwitch(i)
			sl.append(a)

		j=0
		for i in range(0,len(sl)):
			if i+1 != len(sl):
				self.addLink(sl[i],sl[i+1])
			k=0
			while k<y : 
				if k%2==0:
					self.addLink(sl[i],hl[j], bw=1 )
					#r.intf1.config(bw=1)
				else:
					self.addLink(sl[i],hl[j], bw=2 )
					#r.intf1.config(bw=2)
				print i,j
				k=k+1
				j=j+1

#		self.enable_all()

topos= {'mytopo' : (lambda: MyTopo() )}


