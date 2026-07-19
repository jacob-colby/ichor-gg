export interface MineBuild {
  name: string;
  slot_order: string[];
  starter?: { base: string; upgrade: string };
  notes?: string;
}

const KEY = "smite:mine-builds";
const scope = (god: string, mode: string) => `${god}||${mode}`;

type Store = Record<string, MineBuild[]>;

function read(): Store {
  try {
    const raw = localStorage.getItem(KEY);
    const parsed = raw ? JSON.parse(raw) : {};
    return parsed && typeof parsed === "object" ? (parsed as Store) : {};
  } catch {
    return {};
  }
}

function write(store: Store): void {
  localStorage.setItem(KEY, JSON.stringify(store));
}

export function getMine(god: string, mode: string): MineBuild[] {
  return read()[scope(god, mode)] ?? [];
}

export function saveMine(god: string, mode: string, build: MineBuild): void {
  const store = read();
  const k = scope(god, mode);
  const kept = (store[k] ?? []).filter((b) => b.name !== build.name);
  store[k] = [...kept, build];
  write(store);
}

export function deleteMine(god: string, mode: string, name: string): void {
  const store = read();
  const k = scope(god, mode);
  store[k] = (store[k] ?? []).filter((b) => b.name !== name);
  write(store);
}
