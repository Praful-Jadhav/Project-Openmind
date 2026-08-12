export type ConnectionStatus = 'active' | 'disabled';

export interface Connection {
  readonly id: string;
  readonly name: string;
  readonly provider: string;
  readonly capabilities: readonly string[];
  readonly status: ConnectionStatus;
  readonly metadata: Readonly<Record<string, string>>;
  readonly createdAt: Date;
  readonly updatedAt: Date;
}

export interface RegisterConnectionInput {
  readonly id: string;
  readonly name: string;
  readonly provider: string;
  readonly capabilities?: readonly string[];
  readonly metadata?: Readonly<Record<string, string>>;
}

export function createConnection(input: RegisterConnectionInput, now = new Date()): Connection {
  const id = input.id.trim();
  const name = input.name.trim();
  const provider = input.provider.trim();

  if (!id) throw new Error('Connection id is required');
  if (!name) throw new Error('Connection name is required');
  if (!provider) throw new Error('Connection provider is required');

  const capabilities = [...new Set((input.capabilities ?? []).map((value) => value.trim()).filter(Boolean))];
  const metadata = Object.freeze({ ...(input.metadata ?? {}) });

  return Object.freeze({
    id,
    name,
    provider,
    capabilities: Object.freeze(capabilities),
    status: 'active' as const,
    metadata,
    createdAt: now,
    updatedAt: now,
  });
}
