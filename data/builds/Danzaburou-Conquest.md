---
type: smite-build
god: Danzaburou
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fellowship
  aspect_pick_rate: 0.03
  aspect_win_rate: 0.5
  slot_order:
  - name: Transcendence
    pick_rate: 0.31
    win_rate: 0.6
    alternates:
    - name: Tyrfing
      pick_rate: 0.12
      win_rate: 0.32
    - name: Jotunn's Revenge
      pick_rate: 0.08
      win_rate: 0.41
  - name: Jotunn's Revenge
    pick_rate: 0.17
    win_rate: 0.69
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.12
      win_rate: 0.48
    - name: Spear of Desolation
      pick_rate: 0.09
      win_rate: 0.61
  - name: The World Stone
    pick_rate: 0.17
    win_rate: 0.79
    alternates:
    - name: Polynomicon
      pick_rate: 0.09
      win_rate: 0.61
    - name: Silverbranch Bow
      pick_rate: 0.07
      win_rate: 0.33
  - name: Rod of Tahuti
    pick_rate: 0.13
    win_rate: 0.68
    alternates:
    - name: The Executioner
      pick_rate: 0.12
      win_rate: 0.52
    - name: Silverbranch Bow
      pick_rate: 0.08
      win_rate: 0.33
  - name: Qin's Blade
    pick_rate: 0.06
    win_rate: 0.45
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.06
      win_rate: 0.36
    - name: Silverbranch Bow
      pick_rate: 0.05
      win_rate: 0.7
  - name: Void Shard
    pick_rate: 0.04
    win_rate: 0.6
    alternates:
    - name: Skeggox
      pick_rate: 0.04
      win_rate: 0.6
    - name: Titan's Bane
      pick_rate: 0.04
      win_rate: 0.4
  community_starters:
  - name: Conduit Gem
    pick_rate: 0.17
    win_rate: 0.54
  - name: Archmage's Gem
    pick_rate: 0.14
    win_rate: 0.73
  - name: Sharpshooter's Arrow
    pick_rate: 0.11
    win_rate: 0.43
  source_url: https://smitebrain.com/gods/danzaburou/
  last_verified: '2026-08-18'
  god_win_rate: 0.5528846153846154
  god_matches_won: 115
  god_matches_played: 208
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-18'
  god_matches_analyzed: 8839
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Nimble Ring
  - The World Stone
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, The Crusher, Gluttonous Grimoire, Death Metal, Berserker''s
    Shield, Soul Gem, Damaru, Riptalon, Lernaean Bow, Golden Blade, Genji''s Guard,
    The Reaper, Hydra''s Lament, Tekko-Kagi, Runeforged Hammer, The Cosmic Horror,
    Bragi''s Harp, Spear of the Magus, Dominance, Spear of Desolation, Pharaoh''s
    Curse, Breastplate of Valor, Demon Blade, Bracer of The Abyss, Kinetic Cuirass,
    Amanita Charm, Deathbringer, Eye of Providence, Oni Hunter''s Garb, Shogun''s
    Ofuda, Blood-Bound Book, Obsidian Shard, Toxic Blade, Freya''s Tears, Musashi''s
    Dual Swords, Avenging Blade, Silverbranch Bow, Tyrfing.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.49
      win: 0.6
      pick: 0.0
      fit: 0.05
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.64
      win: 0.69
      pick: 0.23
      fit: 0.37
    Transcendence:
      total: 0.49
      efficiency: 0.52
      win: 0.6
      pick: 0.31
      fit: 0.18
    Nimble Ring:
      total: 0.57
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.39
    The World Stone:
      total: 0.56
      efficiency: 0.46
      win: 0.79
      pick: 0.26
      fit: 0.2
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.77
      win: 0.68
      pick: 0.22
      fit: 0.2
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - The Crusher
  - The World Stone
  - Rod of Tahuti
  flex_slots:
  - The Crusher
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Nimble
    Ring, Gluttonous Grimoire, The Crusher, Soul Gem, Death Metal, Genji''s Guard,
    Hydra''s Lament, Berserker''s Shield, Spear of Desolation, Damaru, The Cosmic
    Horror, Breastplate of Valor, Spear of the Magus, Lernaean Bow, Bragi''s Harp,
    Riptalon, Golden Blade, The Reaper, Runeforged Hammer, Bancroft''s Talon, Chronos''
    Pendant, Bracer of The Abyss, Blood-Bound Book, Dominance, Obsidian Shard, Oni
    Hunter''s Garb, Tekko-Kagi, Kinetic Cuirass, Helm of Radiance, Amanita Charm,
    Freya''s Tears, Rod of Asclepius, Pharaoh''s Curse, Eye of Providence, Doom Orb,
    Silverbranch Bow, Tyrfing.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.64
      win: 0.69
      pick: 0.23
      fit: 0.44
    Death Metal:
      total: 0.54
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.51
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.45
    The Crusher:
      total: 0.55
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.39
    The World Stone:
      total: 0.58
      efficiency: 0.46
      win: 0.79
      pick: 0.26
      fit: 0.35
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.77
      win: 0.68
      pick: 0.22
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Death Metal
  - Damaru
  - Demon Blade
  - Rod of Tahuti
  flex_slots:
  - Demon Blade
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, The Crusher, Gluttonous Grimoire, Death Metal, Damaru,
    Soul Gem, Berserker''s Shield, Riptalon, Lernaean Bow, Genji''s Guard, Golden
    Blade, The Reaper, Hydra''s Lament, Tekko-Kagi, The Cosmic Horror, Spear of the
    Magus, Runeforged Hammer, Spear of Desolation, Breastplate of Valor, Pharaoh''s
    Curse, Bragi''s Harp, Demon Blade, Dominance, Kinetic Cuirass, Deathbringer, Bracer
    of The Abyss, Amanita Charm, Eye of Providence, Oni Hunter''s Garb, Blood-Bound
    Book, Obsidian Shard, Musashi''s Dual Swords, Shogun''s Ofuda, Freya''s Tears,
    Toxic Blade, Bancroft''s Talon, Heartseeker, Silverbranch Bow, Tyrfing.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.64
      win: 0.69
      pick: 0.23
      fit: 0.34
    Transcendence:
      total: 0.49
      efficiency: 0.52
      win: 0.6
      pick: 0.31
      fit: 0.15
    Death Metal:
      total: 0.54
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.49
    Damaru:
      total: 0.53
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.44
    Demon Blade:
      total: 0.49
      efficiency: 0.35
      win: 0.6
      pick: 0.0
      fit: 0.67
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.77
      win: 0.68
      pick: 0.22
      fit: 0.2
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Nimble Ring
  - The World Stone
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Gluttonous Grimoire, Nimble Ring, Soul Gem, The Crusher, Spear of Desolation,
    Genji''s Guard, Death Metal, Berserker''s Shield, The Cosmic Horror, Riptalon,
    Hydra''s Lament, Spear of the Magus, Damaru, Breastplate of Valor, The Reaper,
    Lernaean Bow, Obsidian Shard, Golden Blade, Chronos'' Pendant, Tekko-Kagi, Runeforged
    Hammer, Bragi''s Harp, Freya''s Tears, Bracer of The Abyss, Kinetic Cuirass, Blood-Bound
    Book, Amanita Charm, Shield of the Phoenix, Pharaoh''s Curse, Eye of Providence,
    Bancroft''s Talon, Oni Hunter''s Garb, Helm of Radiance, Pendulum Blade, Doom
    Orb, Rod of Asclepius, Dominance, Silverbranch Bow, Tyrfing.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.49
      win: 0.6
      pick: 0.0
      fit: 0.13
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.64
      win: 0.69
      pick: 0.23
      fit: 0.46
    Transcendence:
      total: 0.49
      efficiency: 0.52
      win: 0.6
      pick: 0.31
      fit: 0.13
    Nimble Ring:
      total: 0.56
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.37
    The World Stone:
      total: 0.58
      efficiency: 0.46
      win: 0.79
      pick: 0.26
      fit: 0.33
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.77
      win: 0.68
      pick: 0.22
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Berserker''s Shield, Gluttonous Grimoire, Riptalon,
    Shield of the Phoenix, Nimble Ring, The Crusher, Kinetic Cuirass, The Reaper,
    Rod of Asclepius, Genji''s Guard, Chandra''s Grace, Blood-Bound Book, Pharaoh''s
    Curse, Oni Hunter''s Garb, Golden Blade, Bancroft''s Talon, Runeforged Hammer,
    Death Metal, Damaru, Breastplate of Valor, Phoenix Feather, Freya''s Tears, Spectral
    Armor, Shogun''s Ofuda, Lernaean Bow, Hydra''s Lament, Erosion, Shifter''s Shield,
    Eye of the Storm, Lifebinder, Eye of Providence, Shield Splitter, Umbral Link,
    Leviathan''s Hide, The Cosmic Horror, Draconic Scale, Midgardian Mail.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.49
      win: 0.6
      pick: 0.0
      fit: 0.03
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.64
      win: 0.69
      pick: 0.23
      fit: 0.25
    Transcendence:
      total: 0.49
      efficiency: 0.52
      win: 0.6
      pick: 0.31
      fit: 0.12
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.77
      win: 0.68
      pick: 0.22
      fit: 0.14
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.63
    Soul Gem:
      total: 0.56
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.62
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Nimble Ring
  - The World Stone
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Gluttonous Grimoire, Nimble Ring, Soul Gem, Riptalon,
    The Reaper, Berserker''s Shield, The Cosmic Horror, Death Metal, Tekko-Kagi, Spear
    of the Magus, Damaru, Spear of Desolation, Avenging Blade, Genji''s Guard, Lernaean
    Bow, Golden Blade, Hydra''s Lament, Screeching Gargoyle, Obsidian Shard, Runeforged
    Hammer, Heartseeker, Toxic Blade, Breastplate of Valor, Stone of Binding, Kinetic
    Cuirass, Pharaoh''s Curse, Void Shield, Amanita Charm, Bragi''s Harp, Dominance,
    Pendulum Blade, Eye of Providence, Bracer of The Abyss, Doom Orb, Oni Hunter''s
    Garb, Silverbranch Bow, Titan''s Bane, Tyrfing.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.49
      win: 0.6
      pick: 0.0
      fit: 0.04
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.64
      win: 0.69
      pick: 0.23
      fit: 0.48
    Transcendence:
      total: 0.49
      efficiency: 0.52
      win: 0.6
      pick: 0.31
      fit: 0.15
    Nimble Ring:
      total: 0.56
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.32
    The World Stone:
      total: 0.58
      efficiency: 0.46
      win: 0.79
      pick: 0.26
      fit: 0.35
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.77
      win: 0.68
      pick: 0.22
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Transcendence
  - Nimble Ring
  - Riptalon
  - Rod of Tahuti
  flex_slots:
  - Berserker's Shield
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, The Crusher, Riptalon, Gluttonous Grimoire, Berserker''s
    Shield, Golden Blade, Soul Gem, Death Metal, Damaru, Genji''s Guard, Lernaean
    Bow, Hydra''s Lament, The Reaper, Toxic Blade, The Cosmic Horror, Tekko-Kagi,
    Pharaoh''s Curse, Breastplate of Valor, Runeforged Hammer, Spear of the Magus,
    Spear of Desolation, Kinetic Cuirass, Bragi''s Harp, Bracer of The Abyss, Amanita
    Charm, Dominance, Eye of Providence, Oni Hunter''s Garb, Shogun''s Ofuda, Blood-Bound
    Book, Freya''s Tears, Demon Blade, Obsidian Shard, Deathbringer, Bancroft''s Talon,
    Eros'' Bow, Spectral Armor, Silverbranch Bow, Tyrfing.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.24
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.64
      win: 0.69
      pick: 0.23
      fit: 0.28
    Transcendence:
      total: 0.49
      efficiency: 0.52
      win: 0.6
      pick: 0.31
      fit: 0.13
    Nimble Ring:
      total: 0.56
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.36
    Riptalon:
      total: 0.55
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.6
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.77
      win: 0.68
      pick: 0.22
      fit: 0.17
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - The Crusher
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Nimble Ring, Genji''s Guard,
    Gluttonous Grimoire, The Crusher, Spear of Desolation, Hydra''s Lament, Breastplate
    of Valor, Berserker''s Shield, Death Metal, Freya''s Tears, Chronos'' Pendant,
    Riptalon, Shield of the Phoenix, Damaru, The Cosmic Horror, Lernaean Bow, Spear
    of the Magus, Screeching Gargoyle, Chandra''s Grace, Gem of Focus, Golden Blade,
    The Reaper, Kinetic Cuirass, Totem of Death, Arondight, Runeforged Hammer, Amanita
    Charm, Pharaoh''s Curse, Bracer of The Abyss, Eye of Providence, Pendulum Blade,
    Blood-Bound Book, Oni Hunter''s Garb, Bragi''s Harp, Tekko-Kagi, Obsidian Shard,
    Silverbranch Bow, Tyrfing.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.6
      pick: 0.0
      fit: 0.28
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.64
      win: 0.69
      pick: 0.23
      fit: 0.48
    The Crusher:
      total: 0.54
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.3
    The World Stone:
      total: 0.56
      efficiency: 0.46
      win: 0.79
      pick: 0.26
      fit: 0.2
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.77
      win: 0.68
      pick: 0.22
      fit: 0.2
    Soul Gem:
      total: 0.57
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.65
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Nimble Ring
  - The World Stone
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Nimble Ring, Gluttonous Grimoire, Soul Gem,
    The Crusher, Death Metal, Spear of Desolation, Genji''s Guard, Berserker''s Shield,
    The Cosmic Horror, Spear of the Magus, Hydra''s Lament, Damaru, Riptalon, Breastplate
    of Valor, Chronos'' Pendant, Bragi''s Harp, Lernaean Bow, Bracer of The Abyss,
    Obsidian Shard, The Reaper, Blood-Bound Book, Golden Blade, Runeforged Hammer,
    Bancroft''s Talon, Helm of Radiance, Kinetic Cuirass, Rod of Asclepius, Freya''s
    Tears, Tekko-Kagi, Amanita Charm, Pharaoh''s Curse, Gem of Focus, Eye of Providence,
    Jade Scepter, Oni Hunter''s Garb, Shield of the Phoenix, Doom Orb, Silverbranch
    Bow, Tyrfing.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.49
      win: 0.6
      pick: 0.0
      fit: 0.2
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.64
      win: 0.69
      pick: 0.23
      fit: 0.38
    Transcendence:
      total: 0.49
      efficiency: 0.52
      win: 0.6
      pick: 0.31
      fit: 0.13
    Nimble Ring:
      total: 0.58
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.45
    The World Stone:
      total: 0.58
      efficiency: 0.46
      win: 0.79
      pick: 0.26
      fit: 0.34
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.77
      win: 0.68
      pick: 0.22
      fit: 0.34
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Nimble Ring
  - The World Stone
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Nimble Ring, Gluttonous Grimoire,
    The Crusher, Death Metal, Soul Gem, Berserker''s Shield, Damaru, The Cosmic Horror,
    Riptalon, Spear of the Magus, Lernaean Bow, Spear of Desolation, Genji''s Guard,
    Bragi''s Harp, The Reaper, Golden Blade, Hydra''s Lament, Bracer of The Abyss,
    Runeforged Hammer, Tekko-Kagi, Obsidian Shard, Blood-Bound Book, Breastplate of
    Valor, Bancroft''s Talon, Chronos'' Pendant, Kinetic Cuirass, Dominance, Helm
    of Radiance, Pharaoh''s Curse, Amanita Charm, Rod of Asclepius, Eye of Providence,
    Oni Hunter''s Garb, Deathbringer, Jade Scepter, Doom Orb, Silverbranch Bow, Tyrfing.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.49
      win: 0.6
      pick: 0.0
      fit: 0.18
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.64
      win: 0.69
      pick: 0.23
      fit: 0.36
    Transcendence:
      total: 0.49
      efficiency: 0.52
      win: 0.6
      pick: 0.31
      fit: 0.18
    Nimble Ring:
      total: 0.58
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.45
    The World Stone:
      total: 0.58
      efficiency: 0.46
      win: 0.79
      pick: 0.26
      fit: 0.33
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.77
      win: 0.68
      pick: 0.22
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Nimble Ring
  - Death Metal
  - Gluttonous Grimoire
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Nimble Ring, The Crusher, Gluttonous Grimoire, Death
    Metal, Berserker''s Shield, Soul Gem, Damaru, Riptalon, Lernaean Bow, Golden Blade,
    Genji''s Guard, The Reaper, Hydra''s Lament, Silverbranch Bow, Tekko-Kagi, Tyrfing,
    Runeforged Hammer, The Cosmic Horror, Bragi''s Harp, Spear of the Magus, Dominance,
    Pharaoh''s Curse, Breastplate of Valor, Demon Blade, Bracer of The Abyss, Kinetic
    Cuirass, Amanita Charm, Deathbringer, Spear of Desolation, Eye of Providence,
    Oni Hunter''s Garb, Shogun''s Ofuda, Blood-Bound Book, Obsidian Shard, Toxic Blade,
    Freya''s Tears, Musashi''s Dual Swords, Avenging Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.64
      win: 0.69
      pick: 0.23
      fit: 0.37
    Nimble Ring:
      total: 0.57
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.39
    Death Metal:
      total: 0.54
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.48
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.4
    The Crusher:
      total: 0.56
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.43
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.77
      win: 0.68
      pick: 0.22
      fit: 0.2
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Jotunn's Revenge
  - Nimble Ring
  - Gluttonous Grimoire
  - The Crusher
  - The World Stone
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
  - The World Stone
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Nimble Ring, The Crusher, Gluttonous
    Grimoire, Death Metal, Berserker''s Shield, Soul Gem, Damaru, Riptalon, Lernaean
    Bow, Golden Blade, Genji''s Guard, The Reaper, Hydra''s Lament, Silverbranch Bow,
    Tekko-Kagi, Tyrfing, Runeforged Hammer, The Cosmic Horror, Bragi''s Harp, Spear
    of the Magus, Dominance, Pharaoh''s Curse, Breastplate of Valor, Demon Blade,
    Bracer of The Abyss, Kinetic Cuirass, Amanita Charm, Deathbringer, Spear of Desolation,
    Eye of Providence, Oni Hunter''s Garb, Shogun''s Ofuda, Blood-Bound Book, Obsidian
    Shard, Toxic Blade, Freya''s Tears, Musashi''s Dual Swords, Avenging Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.64
      win: 0.69
      pick: 0.23
      fit: 0.37
    Nimble Ring:
      total: 0.57
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.39
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.4
    The Crusher:
      total: 0.56
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.43
    The World Stone:
      total: 0.56
      efficiency: 0.46
      win: 0.79
      pick: 0.26
      fit: 0.2
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.77
      win: 0.68
      pick: 0.22
      fit: 0.2
  swaps:
  - added: The World Stone
    removed: Death Metal
    reason: community 79% win over 35 matches (vs 55% on this god), taking the model's
      weakest slot from Death Metal
  starter: *id001
---
