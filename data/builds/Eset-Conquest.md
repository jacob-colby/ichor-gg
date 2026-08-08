---
type: smite-build
god: Eset
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Lifewarden
  aspect_pick_rate: 0.35
  aspect_win_rate: 0.56
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.37
    win_rate: 0.57
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.58
    - name: Book of Thoth
      pick_rate: 0.12
      win_rate: 0.67
  - name: Soul Gem
    pick_rate: 0.11
    win_rate: 0.58
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.13
      win_rate: 0.6
    - name: Doom Orb
      pick_rate: 0.09
      win_rate: 0.63
  - name: Rod of Tahuti
    pick_rate: 0.15
    win_rate: 0.63
    alternates:
    - name: Soul Gem
      pick_rate: 0.12
      win_rate: 0.6
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.55
  - name: Obsidian Shard
    pick_rate: 0.13
    win_rate: 0.56
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.21
      win_rate: 0.57
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.6
  - name: Evil Eye
    pick_rate: 0.06
    win_rate: 0.44
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.13
      win_rate: 0.65
    - name: Rod of Tahuti
      pick_rate: 0.09
      win_rate: 0.63
  - name: Void Shard
    pick_rate: 0.06
    win_rate: 0.63
    alternates:
    - name: Evil Eye
      pick_rate: 0.07
      win_rate: 0.48
    - name: Killing Stone
      pick_rate: 0.05
      win_rate: 0.53
  community_starters:
  - name: Conduit Gem
    pick_rate: 0.25
    win_rate: 0.53
  - name: Archmage's Gem
    pick_rate: 0.2
    win_rate: 0.62
  - name: Bumba's Hammer
    pick_rate: 0.11
    win_rate: 0.69
  source_url: https://smitebrain.com/gods/eset/
  last_verified: '2026-08-08'
  god_win_rate: 0.5708154506437768
  god_matches_won: 399
  god_matches_played: 699
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-08'
  god_matches_analyzed: 14443
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Rod of Tahuti
  - Spear of the Magus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Gluttonous Grimoire, Doom Orb, Obsidian Shard, Rod of Tahuti,
    Spear of the Magus, The Cosmic Horror, Genji''s Guard, Chronos'' Pendant, Dreamer''s
    Idol, The World Stone, Gem of Focus, Death Metal, Rod of Asclepius, Blood-Bound
    Book, Helm of Radiance, Breastplate of Valor, Bancroft''s Talon, Jade Scepter,
    Bracer of The Abyss, Wish-Granting Pearl, Polynomicon, Ethereal Staff, Ancient
    Signet, Alchemist Coat, Freya''s Tears.'
  slot_scores:
    Spear of Desolation:
      total: 0.61
      efficiency: 0.52
      win: 0.57
      pick: 0.37
      fit: 1.0
    Doom Orb:
      total: 0.57
      efficiency: 0.49
      win: 0.63
      pick: 0.09
      fit: 0.77
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.77
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.44
      win: 0.63
      pick: 0.15
      fit: 0.77
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.56
      pick: 0.13
      fit: 0.77
    Soul Gem:
      total: 0.62
      efficiency: 0.59
      win: 0.58
      pick: 0.11
      fit: 1.0
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Spear of Desolation
  - Doom Orb
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Rod of Tahuti
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Gluttonous Grimoire, Doom Orb, Genji''s Guard, Obsidian Shard,
    Rod of Tahuti, Spear of the Magus, The Cosmic Horror, Death Metal, Chronos'' Pendant,
    Breastplate of Valor, Dreamer''s Idol, The World Stone, Gem of Focus, Bragi''s
    Harp, Rod of Asclepius, Freya''s Tears, Blood-Bound Book, Helm of Radiance, Bancroft''s
    Talon, Shield of the Phoenix, Jade Scepter, Amanita Charm, Triton''s Conch, Bracer
    of The Abyss, Oni Hunter''s Garb.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.72
      win: 0.55
      pick: 0.07
      fit: 0.22
    Spear of Desolation:
      total: 0.58
      efficiency: 0.52
      win: 0.57
      pick: 0.37
      fit: 0.78
    Doom Orb:
      total: 0.54
      efficiency: 0.49
      win: 0.63
      pick: 0.09
      fit: 0.56
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.44
      win: 0.63
      pick: 0.15
      fit: 0.56
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.56
      pick: 0.13
      fit: 0.56
    Soul Gem:
      total: 0.6
      efficiency: 0.59
      win: 0.58
      pick: 0.11
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shifter's Shield
  - Spear of Desolation
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Amanita Charm, Gluttonous Grimoire, Genji''s Guard, Shield
    of the Phoenix, Rod of Asclepius, Shifter''s Shield, Kinetic Cuirass, Eye of Providence,
    Oni Hunter''s Garb, Blood-Bound Book, Bancroft''s Talon, Chandra''s Grace, Lifebinder,
    Breastplate of Valor, Freya''s Tears, Spear of the Magus, The Cosmic Horror, Phoenix
    Feather, Spectral Armor, Jade Scepter, Erosion, Helm of Radiance, Yogi''s Necklace,
    Draconic Scale, Wish-Granting Pearl.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.72
      win: 0.55
      pick: 0.07
      fit: 0.27
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.6
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.58
      pick: 0.14
      fit: 0.5
    Spear of Desolation:
      total: 0.53
      efficiency: 0.52
      win: 0.57
      pick: 0.37
      fit: 0.5
    Amanita Charm:
      total: 0.58
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.8
    Soul Gem:
      total: 0.61
      efficiency: 0.59
      win: 0.58
      pick: 0.11
      fit: 0.9
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Spear of Desolation
  - Doom Orb
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Rod of Tahuti
  - Spear of the Magus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Soul Gem, Gluttonous Grimoire, Doom Orb, Obsidian Shard, Rod of
    Tahuti, Spear of the Magus, The Cosmic Horror, Genji''s Guard, Dreamer''s Idol,
    The World Stone, Chronos'' Pendant, Screeching Gargoyle, Breastplate of Valor,
    Death Metal, Rod of Asclepius, Blood-Bound Book, Helm of Radiance, Gem of Focus,
    Bancroft''s Talon, Jade Scepter, Bracer of The Abyss, Wish-Granting Pearl, Amanita
    Charm, Polynomicon, Ethereal Staff, Freya''s Tears.'
  slot_scores:
    Spear of Desolation:
      total: 0.61
      efficiency: 0.52
      win: 0.57
      pick: 0.37
      fit: 1.0
    Doom Orb:
      total: 0.58
      efficiency: 0.49
      win: 0.63
      pick: 0.09
      fit: 0.84
    Spear of the Magus:
      total: 0.56
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.84
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.44
      win: 0.63
      pick: 0.15
      fit: 0.84
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.56
      pick: 0.13
      fit: 0.84
    Soul Gem:
      total: 0.62
      efficiency: 0.59
      win: 0.58
      pick: 0.11
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Spear of Desolation
  - Soul Gem
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Gluttonous Grimoire, Genji''s Guard, Obsidian Shard, Spear
    of the Magus, Bracer of The Abyss, Bragi''s Harp, Death Metal, The Cosmic Horror,
    Breastplate of Valor, Nimble Ring, Blood-Bound Book, Bancroft''s Talon, Chronos''
    Pendant, Rod of Asclepius, Amanita Charm, Oni Hunter''s Garb, Helm of Radiance,
    Yogi''s Necklace, Kinetic Cuirass, Jade Scepter, Freya''s Tears, Dreamer''s Idol,
    The World Stone, Gem of Focus, Eye of Providence.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.72
      win: 0.55
      pick: 0.07
      fit: 0.09
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.4
    Nimble Ring:
      total: 0.47
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.48
    Bragi's Harp:
      total: 0.48
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.62
    Spear of Desolation:
      total: 0.52
      efficiency: 0.52
      win: 0.57
      pick: 0.37
      fit: 0.41
    Soul Gem:
      total: 0.56
      efficiency: 0.59
      win: 0.58
      pick: 0.11
      fit: 0.58
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Chronos' Pendant
  - Spear of Desolation
  - Doom Orb
  - Soul Gem
  flex_slots:
  - Chronos' Pendant
  - Doom Orb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Genji''s Guard, Gluttonous
    Grimoire, Breastplate of Valor, Chronos'' Pendant, Doom Orb, Freya''s Tears, Obsidian
    Shard, Shield of the Phoenix, Gem of Focus, Spear of the Magus, The Cosmic Horror,
    Screeching Gargoyle, Chandra''s Grace, Death Metal, Gladiator''s Shield, Amanita
    Charm, Rod of Asclepius, Oni Hunter''s Garb, Dreamer''s Idol, The World Stone,
    Yogi''s Necklace, Blood-Bound Book, Kinetic Cuirass, Helm of Radiance, Bancroft''s
    Talon.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.72
      win: 0.55
      pick: 0.07
      fit: 0.48
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
    Chronos' Pendant:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.63
    Spear of Desolation:
      total: 0.59
      efficiency: 0.52
      win: 0.57
      pick: 0.37
      fit: 0.86
    Doom Orb:
      total: 0.51
      efficiency: 0.49
      win: 0.63
      pick: 0.09
      fit: 0.37
    Soul Gem:
      total: 0.62
      efficiency: 0.59
      win: 0.58
      pick: 0.11
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Spear of Desolation
  - Doom Orb
  - The Crusher
  - Soul Gem
  flex_slots:
  - Doom Orb
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Soul Gem, Jotunn''s Revenge, The Crusher,
    Gluttonous Grimoire, Doom Orb, Genji''s Guard, Hydra''s Lament, Death Metal, Obsidian
    Shard, Spear of the Magus, Lernaean Bow, Bragi''s Harp, Runeforged Hammer, The
    Cosmic Horror, Berserker''s Shield, The Reaper, Golden Blade, Tekko-Kagi, Damaru,
    Heartseeker, Dominance, Bracer of The Abyss, Chronos'' Pendant, Breastplate of
    Valor, Tyrfing, Pendulum Blade, Riptalon, Triton''s Conch, Arondight, Avenging
    Blade, Rod of Asclepius, Titan''s Bane, Silverbranch Bow, Blood-Bound Book, Helm
    of Radiance, Dreamer''s Idol, Bancroft''s Talon, The World Stone, Shield Splitter.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.72
      win: 0.55
      pick: 0.07
      fit: 0.13
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.65
    Spear of Desolation:
      total: 0.54
      efficiency: 0.52
      win: 0.57
      pick: 0.37
      fit: 0.56
    Doom Orb:
      total: 0.52
      efficiency: 0.49
      win: 0.63
      pick: 0.09
      fit: 0.43
    The Crusher:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.63
    Soul Gem:
      total: 0.57
      efficiency: 0.59
      win: 0.58
      pick: 0.11
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - Doom Orb
  - The Crusher
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Doom Orb
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Jotunn''s Revenge, Gluttonous
    Grimoire, The Crusher, Doom Orb, Obsidian Shard, Rod of Tahuti, Genji''s Guard,
    Death Metal, Hydra''s Lament, Spear of the Magus, The Cosmic Horror, Runeforged
    Hammer, The Reaper, Bragi''s Harp, Chronos'' Pendant, Heartseeker, Lernaean Bow,
    Dreamer''s Idol, Triton''s Conch, The World Stone, Damaru, Pendulum Blade, Rod
    of Asclepius, Breastplate of Valor, Blood-Bound Book, Helm of Radiance, Berserker''s
    Shield, Bancroft''s Talon, Gem of Focus, Jade Scepter, Titan''s Bane, Arondight,
    Tekko-Kagi, Bracer of The Abyss, Avenging Blade, Golden Blade, Wish-Granting Pearl,
    Polynomicon.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.7
    Spear of Desolation:
      total: 0.56
      efficiency: 0.52
      win: 0.57
      pick: 0.37
      fit: 0.7
    Doom Orb:
      total: 0.54
      efficiency: 0.49
      win: 0.63
      pick: 0.09
      fit: 0.55
    The Crusher:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.65
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.56
      pick: 0.13
      fit: 0.55
    Soul Gem:
      total: 0.59
      efficiency: 0.59
      win: 0.58
      pick: 0.11
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Chronos' Pendant
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
  - Chronos' Pendant
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Soul Gem, Spear of the Magus, The
    Cosmic Horror, Obsidian Shard, Chronos'' Pendant, Dreamer''s Idol, The World Stone,
    Genji''s Guard, Doom Orb, Gem of Focus, Death Metal, Rod of Asclepius, Rod of
    Tahuti, Blood-Bound Book, Helm of Radiance, Breastplate of Valor, Bancroft''s
    Talon, Jade Scepter, Bracer of The Abyss, Wish-Granting Pearl, Polynomicon, Ethereal
    Staff, Ancient Signet, Alchemist Coat, Freya''s Tears.'
  slot_scores:
    Chronos' Pendant:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.64
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.87
    Spear of Desolation:
      total: 0.61
      efficiency: 0.52
      win: 0.57
      pick: 0.37
      fit: 1.0
    The Cosmic Horror:
      total: 0.54
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.77
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.77
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.56
      pick: 0.13
      fit: 0.77
  starter: *id001
---
