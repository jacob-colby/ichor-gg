---
type: smite-build
god: Aphrodite
mode: Conquest
builds:
- source: community
  aspect: Aspect of Heartbreak
  aspect_pick_rate: 0.6
  aspect_win_rate: 1.0
  slot_order:
  - name: Book of Thoth
    pick_rate: 0.6
    win_rate: 1.0
    alternates:
    - name: Chandra's Grace
      pick_rate: 0.4
      win_rate: 0.5
  - name: Chronos' Pendant
    pick_rate: 0.4
    win_rate: 1.0
    alternates:
    - name: Rod of Asclepius
      pick_rate: 0.2
      win_rate: 0.0
    - name: Freya's Tears
      pick_rate: 0.2
      win_rate: 1.0
  - name: Heartwood Charm
    pick_rate: 0.4
    win_rate: 0.5
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.4
      win_rate: 1.0
    - name: Staff of Myrddin
      pick_rate: 0.2
      win_rate: 1.0
  - name: The World Stone
    pick_rate: 0.2
    win_rate: 1.0
    alternates:
    - name: Gem
      pick_rate: 0.2
      win_rate: 0.0
    - name: Blinking Abyss
      pick_rate: 0.2
      win_rate: 1.0
  - name: Rod of Tahuti
    pick_rate: 0.67
    win_rate: 1.0
    alternates:
    - name: Spear of the Magus
      pick_rate: 0.33
      win_rate: 1.0
  - name: Blinking Abyss
    pick_rate: 0.33
    win_rate: 1.0
    alternates:
    - name: Mote of Chaos
      pick_rate: 0.33
      win_rate: 1.0
    - name: Dreamer's Idol
      pick_rate: 0.33
      win_rate: 1.0
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.6
    win_rate: 1.0
  - name: Sands Of Time
    pick_rate: 0.4
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/aphrodite/
  last_verified: '2026-11-04'
  god_win_rate: 0.8
  god_matches_won: 4
  god_matches_played: 5
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-04'
  god_matches_analyzed: 149
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Gluttonous Grimoire
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  flex_slots:
  - Genji's Guard
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Soul Gem, Amanita Charm, Genji''s Guard, Kinetic
    Cuirass, Obsidian Shard, Breastplate of Valor, Helm of Radiance, Helm of Darkness,
    Blood-Bound Book, Erosion, Shield of the Phoenix, Lotus Sickle, Oni Hunter''s
    Garb, Eye of Providence, Draconic Scale, Ancient Signet, Jade Scepter, Screeching
    Gargoyle, Stone of Binding, Midgardian Mail, Doom Orb, Magi''s Cloak, Leviathan''s
    Hide.'
  slot_scores:
    Book of Thoth:
      total: 0.68
      efficiency: 0.49
      win: 1.0
      pick: 0.6
      fit: 0.19
    Genji's Guard:
      total: 0.73
      efficiency: 0.69
      win: 1.0
      pick: 0.0
      fit: 0.29
    Gluttonous Grimoire:
      total: 0.75
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 0.65
    Spear of Desolation:
      total: 0.76
      efficiency: 0.59
      win: 1.0
      pick: 0.62
      fit: 0.46
    Spear of the Magus:
      total: 0.74
      efficiency: 0.58
      win: 1.0
      pick: 0.71
      fit: 0.33
    Rod of Tahuti:
      total: 0.85
      efficiency: 0.86
      win: 1.0
      pick: 1.0
      fit: 0.33
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Gluttonous Grimoire
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  flex_slots:
  - Genji's Guard
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Gluttonous
    Grimoire, Soul Gem, Genji''s Guard, Amanita Charm, Obsidian Shard, Kinetic Cuirass,
    Breastplate of Valor, Helm of Radiance, Lotus Sickle, Ancient Signet, Death Metal,
    Oni Hunter''s Garb, Helm of Darkness, Blood-Bound Book, Doom Orb, Jade Scepter,
    Shield of the Phoenix, Erosion, Eye of Providence, Screeching Gargoyle, Midgardian
    Mail, Wish-Granting Pearl, Stone of Binding, Polynomicon.'
  slot_scores:
    Book of Thoth:
      total: 0.69
      efficiency: 0.49
      win: 1.0
      pick: 0.6
      fit: 0.24
    Genji's Guard:
      total: 0.73
      efficiency: 0.69
      win: 1.0
      pick: 0.0
      fit: 0.26
    Gluttonous Grimoire:
      total: 0.74
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 0.55
    Spear of Desolation:
      total: 0.74
      efficiency: 0.59
      win: 1.0
      pick: 0.62
      fit: 0.38
    Spear of the Magus:
      total: 0.73
      efficiency: 0.58
      win: 1.0
      pick: 0.71
      fit: 0.29
    Rod of Tahuti:
      total: 0.86
      efficiency: 0.86
      win: 1.0
      pick: 1.0
      fit: 0.35
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Gluttonous Grimoire
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  flex_slots:
  - Genji's Guard
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Gluttonous Grimoire, Soul Gem, Amanita Charm, Genji''s Guard, Obsidian Shard,
    Kinetic Cuirass, Breastplate of Valor, Helm of Radiance, Lotus Sickle, Helm of
    Darkness, Doom Orb, Blood-Bound Book, Shield of the Phoenix, Oni Hunter''s Garb,
    Screeching Gargoyle, Ancient Signet, Death Metal, Erosion, Eye of Providence,
    Midgardian Mail, Jade Scepter, Stone of Binding, Draconic Scale.'
  slot_scores:
    Book of Thoth:
      total: 0.67
      efficiency: 0.49
      win: 1.0
      pick: 0.6
      fit: 0.13
    Genji's Guard:
      total: 0.73
      efficiency: 0.69
      win: 1.0
      pick: 0.0
      fit: 0.25
    Gluttonous Grimoire:
      total: 0.75
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 0.6
    Spear of Desolation:
      total: 0.76
      efficiency: 0.59
      win: 1.0
      pick: 0.62
      fit: 0.46
    Spear of the Magus:
      total: 0.74
      efficiency: 0.58
      win: 1.0
      pick: 0.71
      fit: 0.33
    Rod of Tahuti:
      total: 0.85
      efficiency: 0.86
      win: 1.0
      pick: 1.0
      fit: 0.33
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Spear of the Magus
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Amanita Charm, Gluttonous Grimoire, Shield of the Phoenix,
    Blood-Bound Book, Genji''s Guard, Kinetic Cuirass, Ethereal Staff, Obsidian Shard,
    Bancroft''s Talon, Phoenix Feather, Breastplate of Valor, Yogi''s Necklace, Helm
    of Radiance, Sphere of Negation, Soul Locket, Helm of Darkness, Oni Hunter''s
    Garb, Erosion, Lotus Sickle, Eye of Providence, Jade Scepter, Regrowth Striders,
    Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.73
      efficiency: 0.69
      win: 1.0
      pick: 0.0
      fit: 0.27
    Spear of Desolation:
      total: 0.76
      efficiency: 0.59
      win: 1.0
      pick: 0.62
      fit: 0.46
    Spear of the Magus:
      total: 0.74
      efficiency: 0.58
      win: 1.0
      pick: 0.71
      fit: 0.33
    Rod of Tahuti:
      total: 0.85
      efficiency: 0.86
      win: 1.0
      pick: 1.0
      fit: 0.33
    Amanita Charm:
      total: 0.79
      efficiency: 0.65
      win: 1.0
      pick: 0.0
      fit: 0.76
    Soul Gem:
      total: 0.79
      efficiency: 0.57
      win: 1.0
      pick: 0.0
      fit: 0.94
  community_ordered:
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Gluttonous Grimoire
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Dreamer's Idol
  flex_slots:
  - Dreamer's Idol
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Soul Gem, Obsidian Shard, Amanita Charm, Genji''s
    Guard, Screeching Gargoyle, Stone of Binding, Kinetic Cuirass, Void Stone, Void
    Shield, Breastplate of Valor, Doom Orb, Helm of Radiance, Helm of Darkness, Blood-Bound
    Book, Oni Hunter''s Garb, Lotus Sickle, Shield of the Phoenix, Ancient Signet,
    Erosion, Eye of Providence, Jade Scepter, Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.73
      efficiency: 0.69
      win: 1.0
      pick: 0.0
      fit: 0.24
    Gluttonous Grimoire:
      total: 0.77
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 0.73
    Spear of Desolation:
      total: 0.77
      efficiency: 0.59
      win: 1.0
      pick: 0.62
      fit: 0.55
    Spear of the Magus:
      total: 0.75
      efficiency: 0.58
      win: 1.0
      pick: 0.71
      fit: 0.45
    Rod of Tahuti:
      total: 0.87
      efficiency: 0.86
      win: 1.0
      pick: 1.0
      fit: 0.45
    Dreamer's Idol:
      total: 0.74
      efficiency: 0.51
      win: 1.0
      pick: 1.0
      fit: 0.45
  community_ordered:
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Nimble Ring
  - Bragi's Harp
  - Gluttonous Grimoire
  - Spear of Desolation
  - Rod of Tahuti
  - Eros' Bow
  flex_slots:
  - Eros' Bow
  - Bragi's Harp
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Nimble Ring, Amanita Charm, Soul Gem, Genji''s
    Guard, Kinetic Cuirass, Obsidian Shard, Breastplate of Valor, Helm of Radiance,
    Eros'' Bow, Blood-Bound Book, Helm of Darkness, Ancient Signet, Oni Hunter''s
    Garb, Lotus Sickle, Bragi''s Harp, Bracer of The Abyss, Shield of the Phoenix,
    Screeching Gargoyle, Jade Scepter, Erosion, Death Metal, Midgardian Mail, Stone
    of Binding, Eye of Providence.'
  slot_scores:
    Nimble Ring:
      total: 0.72
      efficiency: 0.63
      win: 1.0
      pick: 0.0
      fit: 0.34
    Bragi's Harp:
      total: 0.68
      efficiency: 0.45
      win: 1.0
      pick: 0.0
      fit: 0.47
    Gluttonous Grimoire:
      total: 0.72
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 0.45
    Spear of Desolation:
      total: 0.73
      efficiency: 0.59
      win: 1.0
      pick: 0.62
      fit: 0.29
    Rod of Tahuti:
      total: 0.83
      efficiency: 0.86
      win: 1.0
      pick: 1.0
      fit: 0.21
    Eros' Bow:
      total: 0.69
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Freya's Tears
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Soul Gem, Amanita
    Charm, Breastplate of Valor, Gluttonous Grimoire, Kinetic Cuirass, Shield of the
    Phoenix, Screeching Gargoyle, Lotus Sickle, Obsidian Shard, Helm of Radiance,
    Oni Hunter''s Garb, Prophetic Cloak, Erosion, Helm of Darkness, Eye of Providence,
    Gem of Focus, Blood-Bound Book, Midgardian Mail, Stone of Binding, Draconic Scale,
    Gladiator''s Shield, Magi''s Cloak, Ancient Signet.'
  slot_scores:
    Book of Thoth:
      total: 0.67
      efficiency: 0.49
      win: 1.0
      pick: 0.6
      fit: 0.08
    Genji's Guard:
      total: 0.75
      efficiency: 0.69
      win: 1.0
      pick: 0.0
      fit: 0.41
    Freya's Tears:
      total: 0.75
      efficiency: 0.58
      win: 1.0
      pick: 0.27
      fit: 0.54
    Spear of Desolation:
      total: 0.76
      efficiency: 0.59
      win: 1.0
      pick: 0.62
      fit: 0.48
    Rod of Tahuti:
      total: 0.83
      efficiency: 0.86
      win: 1.0
      pick: 1.0
      fit: 0.2
    Soul Gem:
      total: 0.75
      efficiency: 0.57
      win: 1.0
      pick: 0.0
      fit: 0.65
  community_ordered:
  - Book of Thoth
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  flex_slots:
  - Gluttonous Grimoire
  - Spear of the Magus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Berserker''s Shield, Jotunn''s Revenge, Gluttonous
    Grimoire, Soul Gem, Amanita Charm, Genji''s Guard, Shield Splitter, Nimble Ring,
    Kinetic Cuirass, Obsidian Shard, Golden Blade, Runeforged Hammer, The Reaper,
    Tekko-Kagi, Hydra''s Lament, Breastplate of Valor, Titan''s Bane, Tyrfing, Helm
    of Radiance, Death Metal, Helm of Darkness, Blood-Bound Book, The Crusher, Oni
    Hunter''s Garb, Toxic Blade, Lotus Sickle, Lernaean Bow, Ancient Signet, Silverbranch
    Bow, Avenging Blade, Eros'' Bow, Bragi''s Harp, Arondight, Heartseeker, Shield
    of the Phoenix, Erosion, Screeching Gargoyle.'
  slot_scores:
    Berserker's Shield:
      total: 0.75
      efficiency: 0.74
      win: 1.0
      pick: 0.0
      fit: 0.29
    Jotunn's Revenge:
      total: 0.75
      efficiency: 0.67
      win: 1.0
      pick: 0.0
      fit: 0.41
    Gluttonous Grimoire:
      total: 0.73
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 0.52
    Spear of Desolation:
      total: 0.74
      efficiency: 0.59
      win: 1.0
      pick: 0.62
      fit: 0.35
    Spear of the Magus:
      total: 0.73
      efficiency: 0.58
      win: 1.0
      pick: 0.71
      fit: 0.26
    Rod of Tahuti:
      total: 0.84
      efficiency: 0.86
      win: 1.0
      pick: 1.0
      fit: 0.26
  community_ordered:
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Spear of Desolation
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Book of Thoth
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Gluttonous Grimoire,
    Soul Gem, Amanita Charm, Genji''s Guard, Shield Splitter, Berserker''s Shield,
    Kinetic Cuirass, Obsidian Shard, Breastplate of Valor, Runeforged Hammer, Helm
    of Radiance, The Reaper, Hydra''s Lament, Titan''s Bane, Helm of Darkness, Blood-Bound
    Book, Death Metal, Lotus Sickle, Ancient Signet, Oni Hunter''s Garb, The Crusher,
    Shield of the Phoenix, Doom Orb, Jade Scepter, Erosion, Eye of Providence, Avenging
    Blade, Screeching Gargoyle, Arondight, Midgardian Mail, Stone of Binding, Heartseeker,
    Draconic Scale, Magi''s Cloak, Leviathan''s Hide.'
  slot_scores:
    Book of Thoth:
      total: 0.68
      efficiency: 0.49
      win: 1.0
      pick: 0.6
      fit: 0.17
    Jotunn's Revenge:
      total: 0.75
      efficiency: 0.67
      win: 1.0
      pick: 0.0
      fit: 0.41
    Transcendence:
      total: 0.66
      efficiency: 0.53
      win: 1.0
      pick: 0.0
      fit: 0.17
    Spear of Desolation:
      total: 0.75
      efficiency: 0.59
      win: 1.0
      pick: 0.62
      fit: 0.41
    Gluttonous Grimoire:
      total: 0.74
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 0.58
    Rod of Tahuti:
      total: 0.85
      efficiency: 0.86
      win: 1.0
      pick: 1.0
      fit: 0.31
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Spear of Desolation
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Soul Gem, Amanita Charm, Genji''s
    Guard, Kinetic Cuirass, Obsidian Shard, Breastplate of Valor, Helm of Radiance,
    Helm of Darkness, Blood-Bound Book, Erosion, Shield of the Phoenix, Lotus Sickle,
    Oni Hunter''s Garb, Eye of Providence, Draconic Scale, Ancient Signet, Jade Scepter,
    Screeching Gargoyle, Stone of Binding, Midgardian Mail, Doom Orb, Magi''s Cloak,
    Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.73
      efficiency: 0.69
      win: 1.0
      pick: 0.0
      fit: 0.29
    Kinetic Cuirass:
      total: 0.73
      efficiency: 0.56
      win: 1.0
      pick: 0.0
      fit: 0.56
    Freya's Tears:
      total: 0.73
      efficiency: 0.58
      win: 1.0
      pick: 0.27
      fit: 0.45
    Spear of Desolation:
      total: 0.76
      efficiency: 0.59
      win: 1.0
      pick: 0.62
      fit: 0.46
    Gluttonous Grimoire:
      total: 0.75
      efficiency: 0.59
      win: 1.0
      pick: 0.0
      fit: 0.65
    Rod of Tahuti:
      total: 0.85
      efficiency: 0.86
      win: 1.0
      pick: 1.0
      fit: 0.33
  community_ordered:
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
---
