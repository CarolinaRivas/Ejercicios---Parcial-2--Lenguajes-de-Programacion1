##Funcion sucesor
def zero(f)
  return lambda {|x| x}
end
Zero = lambda { |f| zero(f) }

#Funcion sucesor
def succ(n)
  return lambda { |f| lambda { |x| f.(n.(f).(x)) } }
end
 
 #Funcion suma
def add(n, m)
  return lambda { |f| lambda { |x| m.(f).(n.(f).(x)) } }
end
 #Funcion multiplicacion
def mult(n, m)
  return lambda { |f| lambda { |x| m.(n.(f)).(x) } }
end
 
 #Funcion que transforma un numero de Chruch a un numero entero
def int_from_couch(f)
  countup = lambda { |i| i+1 }
  f.(countup).(0)
end

 #Funcion que retorna el numero de Chruch
def couch_from_int(x)
  countdown = lambda { |i|
    case i 
      when 0 then Zero 
      else succ(countdown.(i-1))
    end
  }
  countdown.(x)
end

Three = succ(succ(succ(Zero)))
Four  = couch_from_int(4)
Six  = couch_from_int(6)

 
puts [ add(Four,Six ),
       mult(Six,Four )].map {|f| int_from_couch(f) }
