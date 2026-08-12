import assert from 'node:assert/strict';
import test from 'node:test';
import { ConnectionRegistry } from '../src/core/connection-registry.js';

test('registers and retrieves a connection', () => {
  const registry = new ConnectionRegistry();
  const connection = registry.register({
    id: 'github',
    name: 'GitHub',
    provider: 'github',
    capabilities: ['repositories', 'issues'],
  });

  assert.equal(registry.get('github')?.name, 'GitHub');
  assert.deepEqual(connection.capabilities, ['repositories', 'issues']);
});

test('rejects duplicate connection identifiers', () => {
  const registry = new ConnectionRegistry();
  registry.register({ id: 'github', name: 'GitHub', provider: 'github' });

  assert.throws(
    () => registry.register({ id: 'github', name: 'Another GitHub', provider: 'github' }),
    /Connection already exists/,
  );
});

test('filters connections by provider and capability', () => {
  const registry = new ConnectionRegistry();
  registry.register({ id: 'github', name: 'GitHub', provider: 'GitHub', capabilities: ['repositories'] });
  registry.register({ id: 'notion', name: 'Notion', provider: 'Notion', capabilities: ['documents'] });

  assert.equal(registry.filterByProvider('github').length, 1);
  assert.equal(registry.filterByCapability('documents')[0]?.id, 'notion');
});

test('disables a connection without removing its record', () => {
  const registry = new ConnectionRegistry();
  registry.register({ id: 'github', name: 'GitHub', provider: 'github' });

  const disabled = registry.disable('github');

  assert.equal(disabled.status, 'disabled');
  assert.equal(registry.get('github')?.status, 'disabled');
});
