import { createConnection, type Connection, type RegisterConnectionInput } from '../domain/connection.js';

export class ConnectionRegistry {
  private readonly connections = new Map<string, Connection>();

  register(input: RegisterConnectionInput): Connection {
    if (this.connections.has(input.id)) {
      throw new Error(`Connection already exists: ${input.id}`);
    }

    const connection = createConnection(input);
    this.connections.set(connection.id, connection);
    return connection;
  }

  get(id: string): Connection | undefined {
    return this.connections.get(id);
  }

  list(): readonly Connection[] {
    return Object.freeze([...this.connections.values()]);
  }

  filterByProvider(provider: string): readonly Connection[] {
    const normalized = provider.trim().toLowerCase();
    return Object.freeze(
      [...this.connections.values()].filter((connection) => connection.provider.toLowerCase() === normalized),
    );
  }

  filterByCapability(capability: string): readonly Connection[] {
    const normalized = capability.trim().toLowerCase();
    return Object.freeze(
      [...this.connections.values()].filter((connection) =>
        connection.capabilities.some((item) => item.toLowerCase() === normalized),
      ),
    );
  }

  disable(id: string): Connection {
    const current = this.connections.get(id);
    if (!current) throw new Error(`Connection not found: ${id}`);

    const updated = Object.freeze({
      ...current,
      status: 'disabled' as const,
      updatedAt: new Date(),
    });

    this.connections.set(id, updated);
    return updated;
  }

  remove(id: string): boolean {
    return this.connections.delete(id);
  }
}
