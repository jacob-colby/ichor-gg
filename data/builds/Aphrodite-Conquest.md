---
type: smite-build
god: Aphrodite
mode: Conquest
builds:
- source: community
  aspect: Aspect of Heartbreak
  aspect_pick_rate: 0.79
  aspect_win_rate: 0.53
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.32
    win_rate: 0.54
    alternates:
    - name: Book of Thoth
      pick_rate: 0.2
      win_rate: 0.49
    - name: Chandra's Grace
      pick_rate: 0.09
      win_rate: 0.53
  - name: Book of Thoth
    pick_rate: 0.11
    win_rate: 0.62
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.15
      win_rate: 0.53
    - name: The Cosmic Horror
      pick_rate: 0.11
      win_rate: 0.41
  - name: Rod of Tahuti
    pick_rate: 0.18
    win_rate: 0.63
    alternates:
    - name: Totem of Death
      pick_rate: 0.12
      win_rate: 0.44
    - name: Spear of Desolation
      pick_rate: 0.08
      win_rate: 0.59
  - name: Obsidian Shard
    pick_rate: 0.09
    win_rate: 0.56
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.23
      win_rate: 0.54
    - name: Blinking Abyss
      pick_rate: 0.08
      win_rate: 0.65
  - name: Blinking Abyss
    pick_rate: 0.09
    win_rate: 0.54
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.11
      win_rate: 0.62
    - name: Rod of Tahuti
      pick_rate: 0.1
      win_rate: 0.55
  - name: Evil Eye
    pick_rate: 0.09
    win_rate: 0.52
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.11
      win_rate: 0.6
    - name: Killing Stone
      pick_rate: 0.07
      win_rate: 0.58
  community_starters:
  - name: Pendulum of the Ages
    pick_rate: 0.23
    win_rate: 0.64
  - name: Sands Of Time
    pick_rate: 0.2
    win_rate: 0.44
  - name: Archmage's Gem
    pick_rate: 0.18
    win_rate: 0.59
  source_url: https://smitebrain.com/gods/aphrodite/
  last_verified: '2026-11-02'
  god_win_rate: 0.5289017341040463
  god_matches_won: 366
  god_matches_played: 692
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14484
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Genji''s Guard, Kinetic Cuirass, Gluttonous Grimoire,
    Freya''s Tears, Soul Gem, Breastplate of Valor, Helm of Radiance, Helm of Darkness,
    Spear of the Magus, Erosion, Shield of the Phoenix, Lotus Sickle, Eye of Providence,
    Oni Hunter''s Garb, Draconic Scale, Jade Scepter, Chronos'' Pendant, Stone of
    Binding, Screeching Gargoyle, Midgardian Mail, Doom Orb, Magi''s Cloak, Shifter''s
    Shield, The World Stone, Leviathan''s Hide, Mantle Of Discord.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.5
      win: 0.62
      pick: 0.15
      fit: 0.2
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.54
      pick: 0.0
      fit: 0.32
    Spear of Desolation:
      total: 0.54
      efficiency: 0.59
      win: 0.54
      pick: 0.32
      fit: 0.5
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.87
      win: 0.63
      pick: 0.28
      fit: 0.36
    Obsidian Shard:
      total: 0.53
      efficiency: 0.58
      win: 0.56
      pick: 0.15
      fit: 0.46
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Spear of Desolation
  - Breastplate of Valor
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Breastplate of Valor
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Genji''s
    Guard, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass, Breastplate of Valor,
    Soul Gem, Helm of Radiance, Lotus Sickle, Freya''s Tears, Spear of the Magus,
    Death Metal, Helm of Darkness, Oni Hunter''s Garb, Doom Orb, The World Stone,
    Jade Scepter, Chronos'' Pendant, Wish-Granting Pearl, Erosion, Shield of the Phoenix,
    Eye of Providence, Polynomicon, Screeching Gargoyle, Midgardian Mail, Ancient
    Signet, Triton''s Conch, Stone of Binding.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.5
      win: 0.62
      pick: 0.15
      fit: 0.25
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.54
      pick: 0.0
      fit: 0.28
    Spear of Desolation:
      total: 0.53
      efficiency: 0.59
      win: 0.54
      pick: 0.32
      fit: 0.4
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.28
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.87
      win: 0.63
      pick: 0.28
      fit: 0.37
    Obsidian Shard:
      total: 0.52
      efficiency: 0.58
      win: 0.56
      pick: 0.15
      fit: 0.41
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Amanita Charm, Genji''s Guard, Gluttonous Grimoire, Soul Gem, Kinetic Cuirass,
    Freya''s Tears, Breastplate of Valor, Spear of the Magus, Helm of Radiance, Lotus
    Sickle, Helm of Darkness, Doom Orb, Shield of the Phoenix, The World Stone, Oni
    Hunter''s Garb, Screeching Gargoyle, Chronos'' Pendant, Death Metal, Erosion,
    Eye of Providence, Dreamer''s Idol, Jade Scepter, Midgardian Mail, Stone of Binding,
    Draconic Scale, Magi''s Cloak, Leviathan''s Hide.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.5
      win: 0.62
      pick: 0.15
      fit: 0.14
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.54
      pick: 0.0
      fit: 0.27
    Spear of Desolation:
      total: 0.54
      efficiency: 0.59
      win: 0.54
      pick: 0.32
      fit: 0.49
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.87
      win: 0.63
      pick: 0.28
      fit: 0.35
    Obsidian Shard:
      total: 0.53
      efficiency: 0.58
      win: 0.56
      pick: 0.15
      fit: 0.45
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Shield of the Phoenix, Gluttonous Grimoire,
    Kinetic Cuirass, Genji''s Guard, Ethereal Staff, Freya''s Tears, Blood-Bound Book,
    Phoenix Feather, Breastplate of Valor, Rod of Asclepius, Yogi''s Necklace, Helm
    of Radiance, Sphere of Negation, Helm of Darkness, Chandra''s Grace, Spear of
    the Magus, Erosion, Oni Hunter''s Garb, Lotus Sickle, Eye of Providence, Jade
    Scepter, Draconic Scale, Regrowth Striders, Midgardian Mail, Glorious Pridwen.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.6
    Spear of Desolation:
      total: 0.54
      efficiency: 0.59
      win: 0.54
      pick: 0.32
      fit: 0.5
    Obsidian Shard:
      total: 0.53
      efficiency: 0.58
      win: 0.56
      pick: 0.15
      fit: 0.46
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.87
      win: 0.63
      pick: 0.28
      fit: 0.36
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.8
    Soul Gem:
      total: 0.56
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.9
  community_ordered:
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Spear of Desolation
  - Gluttonous Grimoire
  - Rod of Tahuti
  - Obsidian Shard
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
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Amanita Charm, Soul Gem, Genji''s Guard, Screeching
    Gargoyle, Stone of Binding, Spear of the Magus, Kinetic Cuirass, Void Stone, Freya''s
    Tears, Void Shield, Doom Orb, Breastplate of Valor, The World Stone, Helm of Radiance,
    Helm of Darkness, Dreamer''s Idol, Lotus Sickle, Oni Hunter''s Garb, Shield of
    the Phoenix, Erosion, Eye of Providence, Jade Scepter, Chronos'' Pendant, Draconic
    Scale, Midgardian Mail.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.5
      win: 0.62
      pick: 0.15
      fit: 0.17
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.54
      pick: 0.0
      fit: 0.26
    Spear of Desolation:
      total: 0.56
      efficiency: 0.59
      win: 0.54
      pick: 0.32
      fit: 0.59
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.54
      win: 0.54
      pick: 0.0
      fit: 0.7
    Rod of Tahuti:
      total: 0.67
      efficiency: 0.87
      win: 0.63
      pick: 0.28
      fit: 0.48
    Obsidian Shard:
      total: 0.55
      efficiency: 0.58
      win: 0.56
      pick: 0.15
      fit: 0.58
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Book of Thoth
  - Nimble Ring
  - Bragi's Harp
  - Gluttonous Grimoire
  - Rod of Tahuti
  - Eros' Bow
  flex_slots:
  - Book of Thoth
  - Bragi's Harp
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Nimble Ring, Amanita Charm, Soul Gem, Genji''s
    Guard, Kinetic Cuirass, Breastplate of Valor, Freya''s Tears, Helm of Radiance,
    Eros'' Bow, Blood-Bound Book, Spear of the Magus, Helm of Darkness, Lotus Sickle,
    Oni Hunter''s Garb, Bragi''s Harp, Bracer of The Abyss, Jade Scepter, Shield of
    the Phoenix, Chronos'' Pendant, Screeching Gargoyle, Death Metal, Erosion, Midgardian
    Mail, Stone of Binding, Eye of Providence, Doom Orb.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.5
      win: 0.62
      pick: 0.15
      fit: 0.12
    Nimble Ring:
      total: 0.52
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.34
    Bragi's Harp:
      total: 0.47
      efficiency: 0.45
      win: 0.54
      pick: 0.0
      fit: 0.47
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.59
      win: 0.54
      pick: 0.0
      fit: 0.45
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.87
      win: 0.63
      pick: 0.28
      fit: 0.21
    Eros' Bow:
      total: 0.48
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Book of Thoth
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Freya''s Tears, Amanita
    Charm, Breastplate of Valor, Soul Gem, Kinetic Cuirass, Shield of the Phoenix,
    Screeching Gargoyle, Lotus Sickle, Gluttonous Grimoire, Chronos'' Pendant, Helm
    of Radiance, Prophetic Cloak, Oni Hunter''s Garb, Helm of Darkness, Erosion, Eye
    of Providence, Gem of Focus, Gladiator''s Shield, Spear of the Magus, Heartwood
    Charm, Draconic Scale, Stone of Binding, Midgardian Mail, Magi''s Cloak, Chandra''s
    Grace, Leviathan''s Hide.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.5
      win: 0.62
      pick: 0.15
      fit: 0.09
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.54
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.54
      efficiency: 0.59
      win: 0.54
      pick: 0.32
      fit: 0.52
    Freya's Tears:
      total: 0.53
      efficiency: 0.58
      win: 0.54
      pick: 0.0
      fit: 0.58
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.87
      win: 0.63
      pick: 0.28
      fit: 0.21
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Book of Thoth
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Book of Thoth
  - Berserker's Shield
  - Jotunn's Revenge
  - Transcendence
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Book of Thoth
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Berserker''s Shield, Jotunn''s Revenge, Amanita
    Charm, Genji''s Guard, Shield Splitter, Kinetic Cuirass, Golden Blade, Gluttonous
    Grimoire, Runeforged Hammer, Tekko-Kagi, Soul Gem, Hydra''s Lament, Breastplate
    of Valor, Titan''s Bane, Freya''s Tears, Tyrfing, Helm of Radiance, Spear of the
    Magus, Death Metal, Helm of Darkness, The Crusher, Nimble Ring, Toxic Blade, Lotus
    Sickle, Lernaean Bow, Bragi''s Harp, Oni Hunter''s Garb, Silverbranch Bow, Avenging
    Blade, Eros'' Bow, Arondight, Heartseeker, Shield of the Phoenix, Erosion, Jade
    Scepter, Doom Orb, Eye of Providence, Chronos'' Pendant, The Reaper.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.5
      win: 0.62
      pick: 0.15
      fit: 0.14
    Berserker's Shield:
      total: 0.55
      efficiency: 0.74
      win: 0.54
      pick: 0.0
      fit: 0.31
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.67
      win: 0.54
      pick: 0.0
      fit: 0.43
    Transcendence:
      total: 0.46
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.2
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.87
      win: 0.63
      pick: 0.28
      fit: 0.27
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Book of Thoth
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Spear of Desolation
  - Transcendence
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Book of Thoth
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Amanita Charm,
    Genji''s Guard, Shield Splitter, Berserker''s Shield, Gluttonous Grimoire, Kinetic
    Cuirass, Soul Gem, Freya''s Tears, Breastplate of Valor, Runeforged Hammer, Helm
    of Radiance, Hydra''s Lament, Titan''s Bane, Spear of the Magus, Helm of Darkness,
    Death Metal, Lotus Sickle, Oni Hunter''s Garb, The Crusher, Doom Orb, Shield of
    the Phoenix, Jade Scepter, Erosion, Chronos'' Pendant, Eye of Providence, The
    World Stone, Avenging Blade, Heartseeker, Screeching Gargoyle, Draconic Scale,
    Arondight, Stone of Binding, Midgardian Mail, The Reaper, Magi''s Cloak, Dreamer''s
    Idol, Triton''s Conch, Leviathan''s Hide.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.5
      win: 0.62
      pick: 0.15
      fit: 0.18
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.67
      win: 0.54
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.53
      efficiency: 0.59
      win: 0.54
      pick: 0.32
      fit: 0.44
    Transcendence:
      total: 0.46
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.18
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.87
      win: 0.63
      pick: 0.28
      fit: 0.33
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.39
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
  - Spear of Desolation
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Spear of Desolation
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Helm of Darkness — magical protection
    swap_item: Helm of Darkness
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Genji''s Guard, Kinetic Cuirass, Gluttonous
    Grimoire, Freya''s Tears, Soul Gem, Breastplate of Valor, Helm of Radiance, Helm
    of Darkness, Spear of the Magus, Erosion, Shield of the Phoenix, Lotus Sickle,
    Eye of Providence, Oni Hunter''s Garb, Draconic Scale, Jade Scepter, Chronos''
    Pendant, Stone of Binding, Screeching Gargoyle, Midgardian Mail, Doom Orb, Magi''s
    Cloak, Shifter''s Shield, The World Stone, Leviathan''s Hide, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.54
      pick: 0.0
      fit: 0.32
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.6
    Spear of Desolation:
      total: 0.54
      efficiency: 0.59
      win: 0.54
      pick: 0.32
      fit: 0.5
    Freya's Tears:
      total: 0.52
      efficiency: 0.58
      win: 0.54
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.87
      win: 0.63
      pick: 0.28
      fit: 0.36
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  starter: *id001
---
