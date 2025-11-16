from Lead import Lead;

# Criando classe Pencil
class Pencil:
  # Construtor
  def __init__(self, thickness: float):
    self.__thickness = thickness;
    self.__tip: Lead | None = None;
    self.__barrel: list[Lead] = [];
  # Fim construtor

  # Método str
  def __str__(self) -> str:
    return f'calibre: {self.getThickness()}, bico: {self.getTip() if self.getTip() is not None else '[]'}, tambor: <{''.join(list(map(lambda lead: f'{lead}', self.getBarrel())))}>'
  # Fim método str

  # Método de acesso
  def getThickness(self) -> float:
    return self.__thickness;

  def getTip(self) -> Lead | None:
    return self.__tip;

  def getBarrel(self) -> list[Lead]:
    return self.__barrel;
  # Fim método de acesso

  # Método do objeto
  def insert(self, lead: Lead) -> bool:
    if lead.getThickness() != self.getThickness():
      print('fail: calibre incompatível');
      return False;

    self.getBarrel(). append(lead);
    return True;

  def pull(self) -> bool:
    if self.getTip() is not None:
      print('fail: ja existe grafite no bico');
      return False;
  
    self.__tip = self.getBarrel().pop(0);
    return True;

  def remove(self) -> Lead | None:
    if self.getTip() is None:
      print('fail: nao tem grafite no bico');
      return;

    oldLead = self.getTip();
    self.__tip = None;

    return oldLead;

  def write(self):
    if self.getTip() is None:
      print('fail: nao existe grafite no bico');
      return;
  
    if self.getTip().getSize() ==  10 and self.getTip():
      print('fail: tamanho insuficiente');
      return;

    if self.getTip().getSize() - 10 < self.getTip().usagePerSheet():
      print('fail: folha incompleta');
      self.getTip().setSize(10);
      return;

    self.getTip().setSize(self.getTip().getSize() - self.getTip().usagePerSheet());

  # Fim método do objeto
# Fim classe Pencil