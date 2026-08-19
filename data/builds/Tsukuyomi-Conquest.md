---
type: smite-build
god: Tsukuyomi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Mangetsu
  aspect_pick_rate: 0.02
  aspect_win_rate: 0.42
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.38
    win_rate: 0.61
    alternates:
    - name: Transcendence
      pick_rate: 0.31
      win_rate: 0.57
    - name: Hydra's Lament
      pick_rate: 0.1
      win_rate: 0.56
  - name: Transcendence
    pick_rate: 0.22
    win_rate: 0.59
    alternates:
    - name: Book of Thoth
      pick_rate: 0.16
      win_rate: 0.55
    - name: Jotunn's Revenge
      pick_rate: 0.12
      win_rate: 0.55
  - name: Hydra's Lament
    pick_rate: 0.17
    win_rate: 0.56
    alternates:
    - name: Heartseeker
      pick_rate: 0.16
      win_rate: 0.58
    - name: Book of Thoth
      pick_rate: 0.09
      win_rate: 0.54
  - name: Heartseeker
    pick_rate: 0.25
    win_rate: 0.58
    alternates:
    - name: Titan's Bane
      pick_rate: 0.09
      win_rate: 0.55
    - name: The Reaper
      pick_rate: 0.07
      win_rate: 0.62
  - name: Titan's Bane
    pick_rate: 0.12
    win_rate: 0.58
    alternates:
    - name: Heartseeker
      pick_rate: 0.14
      win_rate: 0.65
    - name: Lucerne Hammer
      pick_rate: 0.08
      win_rate: 0.52
  - name: Skeggox
    pick_rate: 0.07
    win_rate: 0.48
    alternates:
    - name: Titan's Bane
      pick_rate: 0.08
      win_rate: 0.67
    - name: Lucerne Hammer
      pick_rate: 0.06
      win_rate: 0.64
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.4
    win_rate: 0.66
  - name: Bumba's Cudgel
    pick_rate: 0.26
    win_rate: 0.5
  - name: Archmage's Gem
    pick_rate: 0.1
    win_rate: 0.55
  source_url: https://smitebrain.com/gods/tsukuyomi/
  last_verified: '2026-08-19'
  god_win_rate: 0.5688545688545689
  god_matches_won: 442
  god_matches_played: 777
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-19'
  god_matches_analyzed: 10108
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - Damaru
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - Damaru
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, The Crusher, Nimble Ring, Gluttonous Grimoire, Death
    Metal, The Reaper, Berserker''s Shield, Damaru, Lernaean Bow, Soul Gem, Golden
    Blade, Tekko-Kagi, Riptalon, Silverbranch Bow, Tyrfing, Genji''s Guard, Bragi''s
    Harp, Runeforged Hammer, The Cosmic Horror, Spear of the Magus, Dominance, Breastplate
    of Valor, Spear of Desolation, Pharaoh''s Curse, Demon Blade, Bracer of The Abyss,
    Kinetic Cuirass, Deathbringer, Obsidian Shard, Amanita Charm, Avenging Blade,
    Toxic Blade, Pendulum Blade, Eye of Providence, Shield Splitter, Oni Hunter''s
    Garb, Shogun''s Ofuda.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.66
      win: 0.58
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.64
      win: 0.61
      pick: 0.38
      fit: 0.49
    Death Metal:
      total: 0.53
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.51
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.63
      win: 0.58
      pick: 0.0
      fit: 0.37
    Damaru:
      total: 0.53
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.44
    The Crusher:
      total: 0.57
      efficiency: 0.64
      win: 0.58
      pick: 0.0
      fit: 0.54
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Crusher
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Nimble Ring, The Crusher, Gluttonous Grimoire, Soul Gem, Death Metal,
    Genji''s Guard, The Reaper, The Cosmic Horror, Berserker''s Shield, Spear of the
    Magus, Spear of Desolation, Breastplate of Valor, Damaru, Bragi''s Harp, Lernaean
    Bow, Golden Blade, Runeforged Hammer, Chronos'' Pendant, Obsidian Shard, Bracer
    of The Abyss, Dominance, Tyrfing, Riptalon, Tekko-Kagi, Bancroft''s Talon, Oni
    Hunter''s Garb, Helm of Radiance, Doom Orb, Silverbranch Bow, The World Stone,
    Blood-Bound Book, Rod of Asclepius, Kinetic Cuirass, Freya''s Tears, Amanita Charm,
    Gem of Focus, Jade Scepter.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.49
      win: 0.55
      pick: 0.22
      fit: 0.28
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.64
      win: 0.61
      pick: 0.38
      fit: 0.52
    Transcendence:
      total: 0.51
      efficiency: 0.52
      win: 0.59
      pick: 0.3
      fit: 0.28
    Hydra's Lament:
      total: 0.53
      efficiency: 0.56
      win: 0.56
      pick: 0.26
      fit: 0.49
    The Crusher:
      total: 0.55
      efficiency: 0.64
      win: 0.58
      pick: 0.0
      fit: 0.44
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.77
      win: 0.58
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - The Crusher
  - Rod of Tahuti
  - Soul Gem
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
    god: Rod of Tahuti, The Crusher, Soul Gem, Gluttonous Grimoire, Nimble Ring, Spear
    of Desolation, Genji''s Guard, The Reaper, The Cosmic Horror, Death Metal, Spear
    of the Magus, Berserker''s Shield, Breastplate of Valor, Riptalon, Damaru, Silverbranch
    Bow, Obsidian Shard, Chronos'' Pendant, Lernaean Bow, Tekko-Kagi, Golden Blade,
    Bragi''s Harp, Runeforged Hammer, Freya''s Tears, Pendulum Blade, Bracer of The
    Abyss, Tyrfing, Kinetic Cuirass, Shield of the Phoenix, Doom Orb, Amanita Charm,
    The World Stone, Gem of Focus, Helm of Radiance, Eye of Providence, Pharaoh''s
    Curse, Blood-Bound Book, Rod of Asclepius.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.49
      win: 0.55
      pick: 0.22
      fit: 0.16
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.64
      win: 0.61
      pick: 0.38
      fit: 0.56
    Transcendence:
      total: 0.49
      efficiency: 0.52
      win: 0.59
      pick: 0.3
      fit: 0.16
    The Crusher:
      total: 0.56
      efficiency: 0.64
      win: 0.58
      pick: 0.0
      fit: 0.5
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.77
      win: 0.58
      pick: 0.0
      fit: 0.4
    Soul Gem:
      total: 0.56
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Reaper
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Rod of Tahuti, The Reaper, Shield
    of the Phoenix, Soul Gem, Gluttonous Grimoire, Kinetic Cuirass, The Crusher, Riptalon,
    Nimble Ring, Rod of Asclepius, Genji''s Guard, Chandra''s Grace, Pharaoh''s Curse,
    Oni Hunter''s Garb, Golden Blade, Runeforged Hammer, Phoenix Feather, Freya''s
    Tears, Breastplate of Valor, Spectral Armor, Death Metal, Blood-Bound Book, Erosion,
    Shogun''s Ofuda, Shifter''s Shield, Eye of the Storm, Damaru, Shield Splitter,
    Eye of Providence, Bancroft''s Talon, Lernaean Bow, Draconic Scale, Lifebinder,
    Leviathan''s Hide, Midgardian Mail, The Cosmic Horror, Avenging Blade, Spear of
    the Magus.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.66
      win: 0.58
      pick: 0.0
      fit: 0.42
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.61
      pick: 0.38
      fit: 0.3
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.58
      pick: 0.0
      fit: 0.49
    The Reaper:
      total: 0.55
      efficiency: 0.52
      win: 0.62
      pick: 0.12
      fit: 0.57
    The Crusher:
      total: 0.54
      efficiency: 0.64
      win: 0.58
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.58
      pick: 0.0
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - The Cosmic Horror
  - Tekko-Kagi
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Tekko-Kagi
  - The Cosmic Horror
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
    for this god: Rod of Tahuti, The Crusher, Gluttonous Grimoire, The Reaper, Soul
    Gem, Nimble Ring, Riptalon, Tekko-Kagi, The Cosmic Horror, Silverbranch Bow, Spear
    of the Magus, Berserker''s Shield, Avenging Blade, Death Metal, Spear of Desolation,
    Damaru, Lernaean Bow, Genji''s Guard, Obsidian Shard, Golden Blade, Toxic Blade,
    Screeching Gargoyle, Runeforged Hammer, Pendulum Blade, Tyrfing, Breastplate of
    Valor, Doom Orb, The World Stone, Bragi''s Harp, Stone of Binding, Kinetic Cuirass,
    Dominance, Pharaoh''s Curse, Void Shield, Amanita Charm, Dreamer''s Idol, Eye
    of Providence, Avatar''s Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.64
      win: 0.61
      pick: 0.38
      fit: 0.6
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.63
      win: 0.58
      pick: 0.0
      fit: 0.53
    The Cosmic Horror:
      total: 0.53
      efficiency: 0.58
      win: 0.58
      pick: 0.0
      fit: 0.43
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.44
      win: 0.58
      pick: 0.0
      fit: 0.76
    The Crusher:
      total: 0.59
      efficiency: 0.64
      win: 0.58
      pick: 0.0
      fit: 0.67
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.77
      win: 0.58
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Riptalon
  - The Crusher
  flex_slots:
  - Golden Blade
  - Berserker's Shield
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
    this god: Nimble Ring, Rod of Tahuti, Riptalon, The Crusher, Gluttonous Grimoire,
    Golden Blade, Berserker''s Shield, Silverbranch Bow, Tyrfing, The Reaper, Soul
    Gem, Lernaean Bow, Genji''s Guard, Death Metal, Damaru, Toxic Blade, Tekko-Kagi,
    The Cosmic Horror, Pharaoh''s Curse, Runeforged Hammer, Breastplate of Valor,
    Spear of the Magus, Bragi''s Harp, Dominance, Bracer of The Abyss, Kinetic Cuirass,
    Amanita Charm, Eye of Providence, Shogun''s Ofuda, Spear of Desolation, Oni Hunter''s
    Garb, Blood-Bound Book, Freya''s Tears, Obsidian Shard, Eros'' Bow, Bancroft''s
    Talon, Qin''s Blade, Demon Blade, Chronos'' Pendant.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.53
      efficiency: 0.66
      win: 0.58
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.61
      pick: 0.38
      fit: 0.3
    Nimble Ring:
      total: 0.56
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.39
    Riptalon:
      total: 0.55
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.65
    The Crusher:
      total: 0.54
      efficiency: 0.64
      win: 0.58
      pick: 0.0
      fit: 0.37
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Soul Gem
  flex_slots:
  - Transcendence
  - Book of Thoth
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Soul Gem, Genji''s
    Guard, Nimble Ring, The Crusher, Breastplate of Valor, Gluttonous Grimoire, Spear
    of Desolation, Chronos'' Pendant, Freya''s Tears, Berserker''s Shield, Shield
    of the Phoenix, Death Metal, The Reaper, The Cosmic Horror, Screeching Gargoyle,
    Gem of Focus, Chandra''s Grace, Spear of the Magus, Damaru, Totem of Death, Riptalon,
    Arondight, Lernaean Bow, Pendulum Blade, Silverbranch Bow, Golden Blade, Runeforged
    Hammer, Kinetic Cuirass, Amanita Charm, Bracer of The Abyss, Bragi''s Harp, Obsidian
    Shard, Pharaoh''s Curse, Tyrfing, Tekko-Kagi, Eye of Providence, Oni Hunter''s
    Garb, Gladiator''s Shield, Helm of Radiance.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.49
      win: 0.55
      pick: 0.22
      fit: 0.1
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.58
      pick: 0.0
      fit: 0.34
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.64
      win: 0.61
      pick: 0.38
      fit: 0.59
    Transcendence:
      total: 0.48
      efficiency: 0.52
      win: 0.59
      pick: 0.3
      fit: 0.1
    Hydra's Lament:
      total: 0.54
      efficiency: 0.56
      win: 0.56
      pick: 0.26
      fit: 0.55
    Soul Gem:
      total: 0.56
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - The Cosmic Horror
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Death Metal
  - The Cosmic Horror
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
    + win/pick). Underrated for this god: Rod of Tahuti, Nimble Ring, Gluttonous Grimoire,
    Soul Gem, The Crusher, Death Metal, The Cosmic Horror, Spear of Desolation, Spear
    of the Magus, Genji''s Guard, The Reaper, Berserker''s Shield, Chronos'' Pendant,
    Bragi''s Harp, Obsidian Shard, Damaru, Breastplate of Valor, Bracer of The Abyss,
    Lernaean Bow, Riptalon, Golden Blade, Silverbranch Bow, Runeforged Hammer, Helm
    of Radiance, Blood-Bound Book, Rod of Asclepius, Tekko-Kagi, Gem of Focus, Freya''s
    Tears, Tyrfing, Doom Orb, Bancroft''s Talon, Totem of Death, Kinetic Cuirass,
    The World Stone, Jade Scepter, Amanita Charm, Shield of the Phoenix, Pharaoh''s
    Curse, Eye of Providence.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.64
      win: 0.61
      pick: 0.38
      fit: 0.46
    Death Metal:
      total: 0.54
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.54
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.63
      win: 0.58
      pick: 0.0
      fit: 0.51
    The Cosmic Horror:
      total: 0.53
      efficiency: 0.58
      win: 0.58
      pick: 0.0
      fit: 0.41
    The Crusher:
      total: 0.55
      efficiency: 0.64
      win: 0.58
      pick: 0.0
      fit: 0.43
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.77
      win: 0.58
      pick: 0.0
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - The Cosmic Horror
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Death Metal
  - The Cosmic Horror
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Nimble Ring, The Crusher,
    Gluttonous Grimoire, Death Metal, Soul Gem, The Reaper, The Cosmic Horror, Spear
    of the Magus, Berserker''s Shield, Bragi''s Harp, Damaru, Lernaean Bow, Spear
    of Desolation, Golden Blade, Genji''s Guard, Tekko-Kagi, Obsidian Shard, Riptalon,
    Runeforged Hammer, Bracer of The Abyss, Silverbranch Bow, Tyrfing, Chronos'' Pendant,
    Breastplate of Valor, Helm of Radiance, Dominance, Blood-Bound Book, Rod of Asclepius,
    Doom Orb, Kinetic Cuirass, The World Stone, Amanita Charm, Pharaoh''s Curse, Triton''s
    Conch, Bancroft''s Talon, Jade Scepter, Eye of Providence.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.64
      win: 0.61
      pick: 0.38
      fit: 0.44
    Death Metal:
      total: 0.55
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.59
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.63
      win: 0.58
      pick: 0.0
      fit: 0.51
    The Cosmic Horror:
      total: 0.53
      efficiency: 0.58
      win: 0.58
      pick: 0.0
      fit: 0.41
    The Crusher:
      total: 0.56
      efficiency: 0.64
      win: 0.58
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.77
      win: 0.58
      pick: 0.0
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Death Metal
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Death Metal
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, The Crusher, Nimble Ring, Gluttonous Grimoire,
    Death Metal, Berserker''s Shield, Damaru, Lernaean Bow, Soul Gem, Golden Blade,
    Tekko-Kagi, Riptalon, Silverbranch Bow, Tyrfing, Genji''s Guard, The Reaper, Bragi''s
    Harp, Runeforged Hammer, The Cosmic Horror, Spear of the Magus, Dominance, Breastplate
    of Valor, Spear of Desolation, Pharaoh''s Curse, Demon Blade, Bracer of The Abyss,
    Kinetic Cuirass, Deathbringer, Obsidian Shard, Amanita Charm, Avenging Blade,
    Toxic Blade, Pendulum Blade, Eye of Providence, Shield Splitter, Oni Hunter''s
    Garb, Shogun''s Ofuda.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.66
      win: 0.58
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.64
      win: 0.61
      pick: 0.38
      fit: 0.49
    Nimble Ring:
      total: 0.55
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.31
    Death Metal:
      total: 0.53
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.51
    The Crusher:
      total: 0.57
      efficiency: 0.64
      win: 0.58
      pick: 0.0
      fit: 0.54
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.77
      win: 0.58
      pick: 0.0
      fit: 0.27
  starter: *id001
---
